"""
Exercício Python 104:
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leiaint(numero):
    ok = False
    valor = 0
    while True:
        n = str(input(numero))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO')
        if ok:
            break
    return valor


num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
