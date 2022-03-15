#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

## eu usei randrange mas ele usa randint
# num = random.randrange(6)

num = randint(0, 5)

user = int(input('Em que número eu pensei? '))
print('Processando...')

if user == num:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num, user))
