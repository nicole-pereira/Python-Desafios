#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot, sqrt
 #o quadrado da hipotenusa é igual a soma dos quadrados do cateto
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

#jeito que eu resolvi
print('A hipotenusa é: {:.2f}'.format(sqrt((co*co)+(ca*ca))))

#tinha um negocio do math só pra isso
hip = hypot(co,ca)
print('A hipotenusa é: {:.2f}'.format(hip))
