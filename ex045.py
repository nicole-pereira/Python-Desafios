#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

opcao = int(input('Qual é a sua jogada? '))

if opcao != 1 or opcao != 0 or opcao != 2:
    print('OPCAO INVALIDA')
    quit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('=-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}' .format(itens[opcao]))
print('=-' * 11)

if opcao == 0 and computador == 1: #jogador jogou pedra e computador jogou papel
    vencedor = 'COMPUTADOR'
elif opcao == 0 and computador == 2: #jogador jogou pedra e computador jogou tesoura
    vencedor = 'JOGADOR'
elif opcao == 1 and computador == 0: #jogador jogou papel e computador jogou pedra
    vencedor = 'JOGADOR'
elif opcao == 1 and computador == 2: #jogador jogou papel e computador jogou tesoura
    vencedor = 'COMPUTADOR'
elif opcao == 2 and computador == 0: #jogador jogou tesoura e computador jogou pedra
    vencedor = 'COMPUTADOR'
elif opcao == 2 and computador == 1: #jogador jogou tesoura e computador jogou papel
    vencedor = 'JOGADOR'
elif opcao == computador:
    vencedor = 'NINGUEM'


print('{} VENCEU'.format(vencedor))
