#Dois jeitos de mostrar o resultado do input
#Exercício Python 2: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

#1
nome = input('Qual seu nome?')
print('É um prazer te conhecer,', nome, '!')

#2
print('É um prazer te conhecer, {}!'.format(nome))

