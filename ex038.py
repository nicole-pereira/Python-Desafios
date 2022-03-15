#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))

if num1 > num2:
    print('O PRIMEIRO VALOR é maior')
elif num1 == num2:
    print('Os valores são IGUAIS')
else:
    print('O SEGUNDO valor é maior')
