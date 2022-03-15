#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

qtd = frase.count('A')
first = frase.find('A')+1
last = frase.rfind('A')+1

print('A letra A aparece {} vezes na frase.\nA primeira letra A apareceu na posição {}\nA última letra A apareceu na posição {}' .format(qtd, first, last))
