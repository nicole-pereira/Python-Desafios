import requests
import copy
import json

"""
Componente que faz a integração com o sistema WeAVA
"""
__author__ = "nicole.pereira"
__date__ = "28/04/2022"
__version__ = open("version").readline()


class WeAVAIntegration(object):
    def __init__(self, cnx=None, log=None):
        try:
            if cnx is None or log is None:
                raise ValueError("Undefined constructor")
            else:
                self.__cnx = cnx
                self.__log = log

            self.status = {
                "success": 'Function success',
                "fail": "Function failed",
                "user_not_found": "User not found or not received",
                "request_fail": "Request response failed",
                "weava_fail": "WeAVA response error"
            }
            self.credentials = self.get_weava_credentials()
        except Exception as ex:
            msg = f"Erro na construção do Autenticador: {str(ex)}"
            log.exception(msg)
            raise Exception(msg)

        """
        self.header = {
            'content-type': 'application/json'
        }"""

    def get_weava_credentials(self):
        """
        Funçao para retornar as credenciais de integração com o WeAVA armazenada no banco
        """
        cursor = self.__cnx.cursor()
        log = self.__log
        query = """
        select array_to_json(array_agg(row_to_json(dt))) from (
            SELECT "value", "alias" FROM "configuration_system"
            WHERE "alias" in ('API_KEY_INTEGRATION_AVVA', 'ENDPOINT_INTEGRATION_AVVA')
        ) dt
        """
        log.database(key="get-weava-credentials",
                     description="buscando credentiais do weava no banco", sql_input=query, cnx=self.__cnx)
        cursor.execute(query)
        credentials = cursor.fetchall()[0][0]
        result_log = copy.deepcopy(credentials)
        for unit in result_log:
            unit['value'] = "*****"
        credentials = {value["alias"]: value["value"] for value in credentials}
        # crendentials = {'API_KEY_INTEGRATION_AVVA': 'value', 'ENDPOINT_INTEGRATION_AVVA'
        log.database_finish(key="get-weava-credentials", success=True, result=result_log)
        return credentials

    def get_user_integration(self, id_user):
        cursor = self.__cnx.cursor()
        log = self.__log
        query = f"""
        select array_to_json(array_agg(row_to_json(dt))) from (
            SELECT u.name, u.email, aic."AVVA_monitoring" avva, aic.telephone_number_list "phone1",
                    aic.contact_emergency, aic.phone_emergency, aic.hashcustomer
            FROM "avva_integration_configuration" aic
            INNER JOIN "user" u on u.id = aic.id_user
            WHERE aic.id_user = {id_user}
        ) dt
        """
        log.database(key="get-user-integration",
                     description="buscando usuario de integração do weava no banco", sql_input=query, cnx=self.__cnx)
        cursor.execute(query)
        user = cursor.fetchall()[0][0]
        user = user[0] if user else None
        log.database_finish(key="get-user-credentials", sucess=True, result=user)

        if not user:
            raise Exception('User integration not found')
        else:
            return user

    def manager_customer(self, id_user=None):
        log = self.__log
        cred = self.credentials
        res = {'result': {}, 'status': self.status['success']}
        try:
            if id_user:
                user_int = self.get_user_integration(id_user)
                avva_event = {
                    "apiKey": cred['API_KEY_INTEGRATION_AVVA'],
                    "nome": f"{user_int['name']}*{user_int['email']}",
                    "description": "Usuario AvaNuv",
                    "email": user_int['email'],
                    "treatmentAvva": user_int['avva'],
                    "phone1": user_int['phone1'],
                    "contactEmergency": user_int['contact_emergency'],
                    "phoneEmergency": user_int['phone_emergency'],
                }
                playload_log = copy.copy(avva_event)
                playload_log['apiKey'] = "*****"
                endpoint_avva = f"{cred['ENDPOINT_INTEGRATION_AVVA']}/api/integrations/customer/managecustomer"
                headers = {'content-type': 'application/json', 'accept': 'application/json'}

                log.request(key='avva-create-customer', description='Criando um cliente no avva', method='POST',
                            url=endpoint_avva, playload=playload_log, header=headers)

                avva_create_customer = requests.post(url=endpoint_avva, json=avva_event, headers=headers)

                if 'json' in avva_create_customer.headers.get('content-type') \
                        and avva_create_customer.status_code != requests.codes.ok:
                    avva_create_customer_json = avva_create_customer.json()
                else:
                    log.request_finish(key='endpoint-avva-analytic', result=avva_create_customer.text,
                                       success=False, response_status=avva_create_customer.status_code)
                    res['status'] = self.status['request_fail']
                    return res

                log.request_finish(key='avva-create-customer', result=avva_create_customer_json, success=True,
                                   response_status=avva_create_customer_json['statusCode'])

                if avva_create_customer_json['statusCode'] != 200:
                    res['status'] = self.status['weava_fail']
                    return res

                res['result']['hashcustomer'] = avva_create_customer_json['results'][0]['data'][0]['hashCustomer']
            else:
                res['status'] = self.status['user_not_found']
                return res
        except Exception as ex:
            raise Exception(ex)
        finally:
            return res

# Resources Analytic Update
    def resetAnalyticAvva(self, analytic_data, analytic_foreignhash, camera, telephones, avva_integration, cod_id,
                          host, lista_hash_class, schedules):
        log = self.__log
        avva_event = {
            "apiKey": self.__api_key,
            "name": analytic_data["alias"],
            "hashCustomer": avva_integration['hashcustomer'],
            "hashCamera": camera['foreignhash'],
            "hashAnalytic": analytic_foreignhash,
            "treatmentAvva": avva_integration['AVVA_monitoring'],
            "aliasAnalytic": analytic_data["alias"],
            "analyticTypeId": analytic_data['id_analytic_type'],
            "streamingUrl": camera['url_source'],
            "liveStreamingUrl": camera['url_view'],
            "aliasCamera": camera['alias'],
            "lat": camera['latitude'],
            "lng": camera['longitude'],
            "username": camera['login'],
            "password": camera['password'],
            "borderColor": analytic_data['border_color'],
            "codId": cod_id,
            "metadata": analytic_data['metadata'],
            "classifier": lista_hash_class,
            "blur": camera['blur'],
            "smallerObjectSize": camera['smaller_object_size'],
            "largerObjectSize": camera['larger_object_size'],
            "schedules": schedules
        }

        avva_event_json = json.dumps(avva_event)

        endpoint_avva_analytic = host + '/api/integrations/analytic/updateanalytic'
        log.request(key="reset-analytic-avva", description="Rollback do update", method="POST",
                    url=endpoint_avva_analytic, payload=avva_event_json, header={'content-type': 'application/json'})

        result = requests.post(
            url=endpoint_avva_analytic,
            json=avva_event_json,
            headers={
                'content-type': 'application/json'
            }
        )
        log.request_finish(key="reset-analytic-avva", result=result.content.decode(
            'utf-8'), success=True, response_status=result.status_code)
        return "dataError"

    def updateAnalyticAvva(self, avva_event, host):
        log = self.__log
        avva_event_json = avva_event
        payload_log = copy.copy(avva_event_json)
        payload_log['username'] = "*****"
        payload_log['password'] = "*****"
        payload_log['streamingUrl'] = "*****"
        endpoint_avva_analytic = host + '/api/integrations/analytic/updateanalytic'
        log.request(key='update-analytic-avva', description="Atualizando o analítico no Avva", method="POST",
                    url=endpoint_avva_analytic, payload=payload_log, header={'content-type': 'application/json'})
        avva_analytic = requests.post(
            url=endpoint_avva_analytic,
            json=avva_event_json,
            headers={
                'content-type': 'application/json'
            }
        )
        success_comunication = avva_analytic.status_code == requests.codes.ok
        avva_analytic_json = json.loads(avva_analytic.content.decode('utf-8'))
        success_update = avva_analytic_json['statusCode'] == 200

        log.request_finish(key="update-analytic-avva", result=avva_analytic_json,
                           success=success_update, response_status=avva_analytic_json['statusCode'])

        if not success_comunication:
            return False, "errorRequest"
        if not success_update:
            return False, "errorAvva"

        return True, "Success"

# Resources Users Activeanalytics
    def rollbackAvva(self, host_avva, hashcustomer, api_key):
        log = self.__log
        avva_event_delete_customer = {
            "hashCustomer": hashcustomer,
            "apiKey": api_key
        }
        payload_log = copy.copy(avva_event_delete_customer)
        payload_log['apiKey'] = "*****"

        endpoint_avva_remove_customer = host_avva + '/api/integrations/customer/deletecustomer'

        log.request(key='rollback-avva', description='Desfazendo as operações anteriores', method='POST',
                    url=endpoint_avva_remove_customer, payload=payload_log, header={'content-type': 'application/json'})

        requests.post(
            url=endpoint_avva_remove_customer,
            json=avva_event_delete_customer,
            headers={
                'content-type': 'application/json'
            }
        )
        log.request_finish(key='rollback-avva', result=None, success=True, response_status=200)

    def rollback_device_avva(self, hashdevice, apikey, host_avva):
        log = self.__log
        avva_event_delete_device = {
            "apiKey": apikey,
            "hashDevice": hashdevice
        }
        payload_log = copy.copy(avva_event_delete_device)
        payload_log['apiKey'] = "*****"
        endpoint_avva_delete_device = host_avva + '/api/integrations/device/deletedevice'
        log.request(
            key='rollback-device-avva',
            description='Removendo o dispositivo criado',
            method='POST',
            url=endpoint_avva_delete_device,
            payload=payload_log,
            header={
                'content-type': 'application/json'
            }
        )
        requests.post(
            url=endpoint_avva_delete_device,
            json=avva_event_delete_device,
            headers={
                'content-type': 'application/json'
            }
        )
        log.request_finish(
            key='rollback-device-avva',
            result=None,
            success=True,
            response_status=200
        )

    def createDevice(self, cnx, alias: str, hash_customer: str, api_key: str, host_avva):
        cursor = self.__connection.cursor()
        log = self.__log

        header = {"content-type: application/json"}
        payload = {
            "alias": alias,
            "hashCustomer": hash_customer,
            "apiKey": api_key
        }
        payload_log = copy.deepcopy(payload)
        payload_log["apiKey"] = "******"
        endpoint_avva_create_device = "".join(
            [host_avva, '/api/integrations/device/createdevice'])
        log.request(
            key='create-device',
            description='Criando dispositivo no avva',
            method="POST",
            payload=payload_log,
            header={
                'content-type': 'application/json'
            },
            url=endpoint_avva_create_device
        )
        avva_create_device = requests.post(
            url=endpoint_avva_create_device,
            json=payload,
            headers={
                'content-type': 'application/json'
            },
        )
        if avva_create_device.status_code != requests.codes.ok:
            log.request_finish(key='create-device', result=avva_create_device.json(), success=True,
                               response_status=avva_create_device.status_code)
            return "erroRequest"

        avva_create_device_json = avva_create_device.json()

        if avva_create_device_json['statusCode'] != 200:
            log.request_finish(key='create-device', result=avva_create_device_json, success=True,
                               response_status=avva_create_device_json['statusCode'])
            return "errorAPIAvva"

        log.request_finish(key='create-device', result=avva_create_device_json, success=True, response_status=200)

        hash_device = avva_create_device_json['results'][0]['data'][0]['hashDevice']

        if hash_device:
            qry_insert_device = "\
                INSERT INTO device (alias, hashname, panic_status, id_customer) \
                    SELECT %s, %s, %s, c.id \
                    FROM customer c \
                    WHERE c.id_user = (SELECT aic.id_user FROM avva_integration_configuration aic WHERE aic.hashcustomer = %s)"
            log.database(
                key="insert-device",
                description="Inserindo dispositivo criado do avva no avanuv",
                cnx=cnx,
                sql_input=qry_insert_device
            )
            cursor.execute(qry_insert_device, (alias, hash_device, False, hash_customer))

            if cursor.rowcount == 0:
                rollback_device_avva(log=log, hashdevice=hash_device, apikey=api_key, host_avva=host_avva)
            log.database_finish(
                key='insert-device',
                success=True,
                result=None
            )

# Resources Users DeleteClient
    def deleteCustomerAvva(self, child_id, configs, cnx):
        # Busca o hashcustomer para enviar na requisição ao Avva
        cursor = self.__connection.cursor()
        log = self.__log
        qry = f"""
            SELECT aic.hashcustomer FROM public.avva_integration_configuration aic
            WHERE id_user = %s
        """
        log.database(key='get-hashcustomer',
                     description='Obtendo hashcustomer da integração com o avva', sql_input=qry, cnx=cnx)
        cursor.execute(cursor.mogrify(qry, (child_id,)))
        hashcustomer = cursor.fetchall()
        hashcustomer = hashcustomer[0][0] if hashcustomer else None
        log.database_finish(key='get-hashcustomer', success=True)

        if hashcustomer:
            # Requisição de deletar customer do Avva
            avva_event = {
                "hashCustomer": hashcustomer,
                "apiKey": configs['API_KEY_INTEGRATION_AVVA']
            }
            headers = {
                'content-type': 'application/json'
            }
            endpoint_avva_analytic = "".join(
                [configs['ENDPOINT_INTEGRATION_AVVA'], '/api/integrations/customer/deletecustomer'])
            log.request(key='delete-customer-request', description='Requisição para deletar customer do Avva',
                        method='POST', url=endpoint_avva_analytic, payload=avva_event, header=headers)
            res = requests.post(url=endpoint_avva_analytic, json=avva_event, headers=headers)
            res_api = json.loads(res.content.decode('utf-8'))
            log.request_finish(key='delete-customer-request', success=True, result=res_api,
                               response_status=res.status_code)
            if 'statusCode' in res_api:
                if str(res_api['statusCode']) != "200" and str(res_api['statusCode']) != "404":
                    raise requestError(str(res_api))
            else:
                raise requestError(str(res_api))

# Resources Users UpdateClientInfo
    def updateCustomerAvva(self, api_key, host_avva, name, email, telephone, contact_emergency,
                           phone_emergency, avva, hashcustomer, cnx):
        cursor = self.__connection.cursor()
        log = self.__log
        avva_event = {
            "apiKey": api_key,
            "name": f"{name}*{email}",
            "description": "Usuario AvaNuv",
            "email": email,
            "treatmentAvva": avva,
            "phone1": telephone,
            "contactEmergency": contact_emergency,
            "phoneEmergency": phone_emergency,
            "hashCustomer": hashcustomer
        }
        payload_log = copy.copy(avva_event)
        payload_log['apiKey'] = "*****"
        endpoint_avva = "".join(
            [host_avva, '/api/integrations/customer/managecustomer'])

        log.request(key='avva-update-customer', description='Atualizando um cliente no avva', method='POST',
                    url=endpoint_avva, payload=payload_log, header={'content-type': 'application/json'})

        avva_create_customer = requests.post(
            url=endpoint_avva,
            json=avva_event,
            headers={
                'content-type': 'application/json'
            }
        )
        avva_create_customer_json = json.loads(avva_create_customer.content.decode("utf-8"))
        msgAvva = avva_create_customer_json['results'][0]['message']
        log.request_finish(key='avva-update-customer', result=msgAvva, success=True,
                           response_status=avva_create_customer_json['statusCode'])

        if avva_create_customer.status_code != requests.codes.ok:
            raise erroRequest('Erro na requisição.')

        if avva_create_customer_json['statusCode'] != 200:
            raise errorAPIAvva('errorAPIAvva')

    def delete_device_avva(self, hashdevice, apikey, host_avva):
        log = self.__log
        avva_event_delete_device = {
            "apiKey": apikey,
            "hashDevice": hashdevice
        }
        payload_log = copy.copy(avva_event_delete_device)
        payload_log['apiKey'] = "*****"
        endpoint_avva_delete_device = host_avva + '/api/integrations/device/deletedevice'
        log.request(
            key='delete-device-avva',
            description='Removendo o dispositivo do Avva',
            method='POST',
            url=endpoint_avva_delete_device,
            payload=payload_log,
            header={
                'content-type': 'application/json'
            }
        )
        requests.post(
            url=endpoint_avva_delete_device,
            json=avva_event_delete_device,
            headers={
                'content-type': 'application/json'
            }
        )
        log.request_finish(
            key='delete-device-avva',
            result=None,
            success=True,
            response_status=200
        )

# CreateDevice Resources Users UpdateClientInfo não usado, pois já tem um

# Serves Scheduling Create Analytic Async
    def createAnalyticOnAvva(self, avva_body, config_system):
        log = self.__log
        status = 'success'
        avva_analytic_endpoint = f"{config_system['ENDPOINT_INTEGRATION_AVVA']}/api/integrations/analytic/startanalytic"
        avva_header = {'content-type': 'application/json', 'accept': 'application/json'}

        payload_log = copy.copy(avva_body)
        payload_log['password'] = "*****"

        log.request(key='endpoint-avva-analytic', description='Enviando os analiticos para o avva', method='POST',
                    url=avva_analytic_endpoint, payload=payload_log, header=avva_header)

        avva_analytic = requests.post(url=avva_analytic_endpoint, json=avva_body, headers=avva_header, timeout=60)

        if 'json' in avva_analytic.headers.get('content-type'):
            res_avva_analytic = avva_analytic.json()
        else:
            log.request_finish(key='endpoint-avva-analytic', result=avva_analytic.text,
                               success=False, response_status=avva_analytic.status_code)
            status = "errorRequest"
            return 0, status

        log.request_finish(key='endpoint-avva-analytic', result=res_avva_analytic,
                           success=True, response_status=avva_analytic.status_code)

        if avva_analytic.status_code != requests.codes.ok:
            status = "errorRequest"
            return 0, status

        if res_avva_analytic['statusCode'] != 200:
            status = "errorAvva"
            return 0, status

        return res_avva_analytic, status

    def deleteAnalyticAvva(self, config_system, avva_analytic):
        log = self.__log
        avva_delete = {
            "apiKey": config_system['API_KEY_INTEGRATION_AVVA'],
            "hashAnalytic": avva_analytic['results'][0]['data'][0]['hashAnalytic']
        }

        endpoint_avva = "".join(
            [config_system['ENDPOINT_INTEGRATION_AVVA'], "/api/integrations/analytic/removeanalytic"])

        log.request(key='delete-analytic-avva', description='Removendo os analiticos do avva', method='POST',
                    url=endpoint_avva, payload=avva_delete, header={'content-type': 'application/json'})

        avva_remove_analytic = requests.post(
            url=endpoint_avva,
            json=avva_delete,
            headers={
                'content-type': 'application/json'
            }
        )
        log.request_finish(key='delete-analytic-avva', result=None, success=True, response_status=200)
        status = "dataError"
        return status

# Serves Scheduling Delete Client Async
# delete_device_avva igual

    def deleteCamera(self, cnx, cursor, log, camera_id, result_hashname):
        wowza = WowzaFunctions(cursor, log)
        configs = getSystemConfigurations(log, cnx, cursor)
        if result_hashname['foreignhash']:
            avva_event = {
                "hashCamera": result_hashname['foreignhash'],
                "apiKey": configs['API_KEY_INTEGRATION_AVVA']
            }
            headers = {
                'content-type': 'application/json'
            }
            endpoint_avva_analytic = "".join(
                [configs['ENDPOINT_INTEGRATION_AVVA'], '/api/integrations/camera/deletecamera'])
            log.request(key='avva-delete-camera', description='Removendo uma camera do avva', method='POST',
                        url=endpoint_avva_analytic, payload=avva_event, header={'content-type': 'application/json'})

            res = requests.post(url=endpoint_avva_analytic, timeout=60, json=avva_event, headers=headers)
            res_api = json.loads(res.content.decode('utf-8'))
            log.request_finish(key='avva-delete-camera', success=True, result=res_api, response_status=res.status_code)
            if res_api['statusCode'] != 200 and res_api['statusCode'] != 404:
                return False

        # Chamando a função para remover do wowza
        # delete_wowza(config_system, result_hashname, log)
        wowza.stop_recording(result_hashname['hashname'])
        wowza.disconnect_streamfile(result_hashname['hashname'])
        wowza.delete_startup(result_hashname['hashname'])
        wowza.remove_streamfile(result_hashname['hashname'])

        # Query para setar a flag do delete como True e o active como False
        qry_delete_camera_table = f''' update camera set "deleted" = true, active = false where id = %(camera)s;
        update camera_history set final_date = NOW() where id_camera = %(camera)s and final_date isnull;'''

        log.database(key="qry-delete-camera",
                     description="Setando a flag do delete como True e o active como False",
                     sql_input=str(cursor.mogrify(qry_delete_camera_table, {'camera': camera_id})), cnx=cnx)
        cursor.execute(qry_delete_camera_table, {'camera': camera_id})
        log.database_finish(key="qry-delete-camera", result=None, success=True)

        deleteCameraMosaic(camera_id, log, cursor, cnx)
        delete_analytic_schedule(camera_id, cursor, cnx, log)

        cnx.commit()
        return True

# deleteCustomer igual

# Servers Scheduling Doublecheck Avva
    def send_check_avva(self, log, base_url, api_key, hash_check, page, total_pages, resouces=[], type_send='clients'):
        status = 'fail'
        res = [page]
        payload = {
            "type": type_send,
            "resources": resouces,
            "offset": page,
            "full_offset": total_pages,
            "identifier": hash_check,
            "apiKey": api_key
        }
        headers = {'content-type': 'application/json'}
        url = base_url + "/api/integrations/service/doublecheck"
        payload_log = copy.copy(payload)
        payload_log['apiKey'] = "*****"

        for i in range(3):
            log.request(key=f"start-checking-request-{type_send}",
                        description='Requisição de verificação dos analíticos',
                        method='POST', url=url, payload=payload_log, header=headers)
            response = requests.post(url=url, json=payload, headers=headers, timeout=60)

            if response.status_code == requests.codes.ok:
                response = response.json()
                log.request_finish(key=f"start-checking-request-{type_send}", success=True,
                                   result=response, response_status=response['statusCode'])

                if response['statusCode'] in [200]:
                    return 'success', response[0]['data'][0]['pages']
                elif response['statusCode'] in [404, 201]:
                    return 'missing', response[0]['data'][0]['pages']
                elif response['statusCode'] in [409, 202]:
                    return 'repeat', response[0]['data'][0]['pages']
                else:
                    status = 'fail'
                    res = response[0]['data'][0]['pages'] if response and response[0]['data'] else res
            else:
                status = 'fail'

        return status, res

    # Serves Scheduling Update Analytic Async
    def updateAnalyticOnAvva(self, avva_body, config_system, log):
        status = 'success'
        avva_analytic_endpoint = "".join(
            [config_system['ENDPOINT_INTEGRATION_AVVA'], '/api/integrations/analytic/updateanalytic'])
        avva_header = {
            'content-type': 'application/json',
        }

        payload_log = copy.copy(avva_body)
        payload_log['streamingUrl'] = "*****"
        payload_log['username'] = "*****"
        payload_log['password'] = "*****"

        log.request(key='endpoint-avva-analytic', description='Enviando os analiticos para o avva', method='POST',
                    url=avva_analytic_endpoint, payload=payload_log, header=avva_header)

        avva_analytic = requests.post(
            url=avva_analytic_endpoint,
            json=avva_body,
            headers=avva_header,
            timeout=60
        )
        if avva_analytic.status_code != requests.codes.ok:
            log.request_finish(key='endpoint-avva-analytic', result=avva_analytic.json(),
                               success=False, response_status=avva_analytic.status_code)
            status = "errorRequest"
            return 0, status

        avva_analytic = json.loads(avva_analytic.content.decode("utf-8"))

        if avva_analytic['statusCode'] != 200:
            log.request_finish(key='endpoint-avva-analytic', result=avva_analytic,
                               success=False, response_status=avva_analytic['statusCode'])
            status = "errorAvva"
            return 0, status
        log.request_finish(key='endpoint-avva-analytic', result=avva_analytic,
                           success=True, response_status=avva_analytic['statusCode'])
        return avva_analytic, status
