# função

# entre o def e o programa principal é necessário ter duas linhas

def lin():
    # padrao
    print('-' * 20)


lin()
print('Curso em Video')
lin()
print('Aprenda Python')
lin()


def mensagem(msg):
    # com parametro
    lin()
    print(msg)
    lin()


mensagem('Amo o Baekhyun')


def soma(a, b):
    # com parametro
    print(f'\nA = {a} + B = {b}')
    s = a + b
    print(f'A soma A + B = {s}\n')


soma(5, 5)
# explicitando
soma(b=3, a=4)


def contador(* num):
    # tuplas
    # empacotamento
    # * significa desempacotamento
    # conta os numeros de maneira ilimitada
    ''' for valor in num:
        print(f'{valor} ', end='')
    print('FIM!') '''
    tam = len(num)
    print(f'\nRecebi os valores {num} e são ao todo {tam} numeros')


contador(2, 1, 7)
contador(9, 0)
contador(6, 1, 4, 0, 7)


def somar(* valor):
    sr = 0
    for num in valor:
        sr += num
    print(f'\nSomando os valores {valor} temos {sr}\n')


somar(4, 6, 1, 4)

# listas não precisam de desempacotamento


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [4, 6, 7, 9, 1, 2]
dobra(valores)
print(valores)
