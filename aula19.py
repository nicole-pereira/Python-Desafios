
#primeiro exemplo
pessoas = {'nome': 'Nicole', 'sexo': 'F', 'idade': 21}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')

#isso funciona sem precisar do append
pessoas['nome'] = 'Marisa'
pessoas['peso'] = 70.5

print(pessoas.keys())
for k in pessoas.keys():
    print(k)

print(pessoas.values())
for k in pessoas.values():
    print(k)

print(pessoas.items())
for k in pessoas.items():
    print(k)
#items no lugar do enumerate
for k, v in pessoas.items():
    print(f'{k} = {v}')


#dicionario dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Pernambuco', 'sigla': 'PE'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1])
print(brasil[1]['sigla'])
print(brasil[0])
print(brasil[0]['uf'])


#fatiamento dos dados (cópia)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy())

#for de fora = lista
#for de dentro = dicionario
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}\n')
    '''for v in e.values():
        print(v, end=' ')
'''
