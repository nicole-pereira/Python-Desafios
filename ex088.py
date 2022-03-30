#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

linha = ('-'*17)

print(linha)
print('JOGA NA MEGA SENA')
print(linha)
num = int(input('Quantos jogos você quer que eu sorteie? '))

jogo = []
lista = []
total = 1

while total <= num:
    cont = 0
    while True:
        n = randint(1, 61)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.append(jogo[:])
    jogo.clear()
    total += 1
    jogo.sort()

print('=-' * 5 + f' SORTEANDO {num} JOGOS ' + '-=' * 5)
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    sleep(0.7)
print('=-' * 5 + ' BOA SORTE ' + '-=' * 5)
