#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número: '))

print('--' * 12)
print('{} x {:2} = {}\n{} x {:2} = {}\n{} x {:2} = {}\n{} x {:2} = {}' .format(num, 1, (num*1), num, 2, (num*2), 3, num, (num*3), 4, num, (num*4)), end=' ')
print('\n{} x {:2} = {}\n{} x {:2} = {}\n{} x {:2} = {}\n{} x {:2} = {}\n{} x {:2} = {}\n{} x {:2} = {}'.format(num, 5, (num*5), num, 6, (num*6), num, 7, (num*7), num, 8, (num*8), num, 9, (num*9), num, 10, (num*10)))
print('--' * 12)
