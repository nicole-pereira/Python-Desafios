#Exercício Python 18: Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

num = float(input('Digite o ângulo: '))


print('O ângulo de {} tem o SENO de {:.2f}' .format(num, (sin(radians(num)))))
print('O ângulo de {} tem o COSSENO de {:.2f}' .format(num, (cos(radians(num)))))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(num, (tan(radians(num)))))



