#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

computador = randint(0, 10)
cont = 0
acertou = False

while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    cont += 1
    if palpite == computador:
        acertou = True
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
        acertou = False
    elif palpite < computador:
        print('Mais... Tente mais uma vez.')
        acertou = False

print('Acertou com {} tentativas. Parabéns!'.format(cont))

