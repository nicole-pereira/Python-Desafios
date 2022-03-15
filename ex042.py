#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('É um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('ISÓSCELES!')
    elif r1 != r2 != r3:
        print('ESCALENO!')
else:
    print('Não se forma um triângulo.')
