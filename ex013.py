#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o valor do salário do funcionário? R$'))

aumento = salario + (salario * 0.15)

print('Um funiconário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.' .format(salario, aumento))
