#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maior = 0
menor = 0
anoAtual = date.today().year

for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = anoAtual - ano
    if idade >= 19:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
