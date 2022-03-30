#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)),
       (randint(1, 10)), (randint(1, 10)))

print(f'Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')

print(f'\nO menor valor sorteado foi o {min(num)}')
print(f'O maior valor sorteado foi o {max(num)}')
