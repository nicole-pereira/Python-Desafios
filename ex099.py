'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep


def verMaior(num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    sleep(0.3)
    tam = len(num)
    for n in num:
        print(f'{n} ', end='')
        sleep(0.3)
    if num != []:
        print(f'Foram informados {tam} valores ao todo\n{max(num)} é o maior')
    else:
        print('Foram informados 0 valores ao todo.')


lista = [2, 9, 4, 5, 7, 1]
verMaior(lista)

lista = [4, 7, 0]
verMaior(lista)

lista = [1, 2]
verMaior(lista)

lista = [6]
verMaior(lista)

lista = []
verMaior(lista)
