'''Exercício Python 100:
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista,
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint


def sorteia(lista):
    for c in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
    print(f'Sorteando... {lista}')


def somapar(lista):
    sp = 0
    for n in lista:
        if n % 2 == 0:
            sp += n
    print(f'Somando os valores pares de {lista} temos {sp}')


numeros = []
sorteia(numeros)
somapar(numeros)
