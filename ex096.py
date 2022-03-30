'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def area(a, b):
    m = a * b
    print(f'A área de um tereno {a}x{b} é de {m}m²')


print('    Controle de Terrenos    ')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

