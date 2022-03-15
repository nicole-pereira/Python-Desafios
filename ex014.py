#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Informe a temperatura em C: '))
conv = celsius * 1.8 + 32

print('A temperatura em {}ºC corresponde a {}ºF'.format(celsius, conv))
