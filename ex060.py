#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um númmero para\ncalcular seu FATORIAL: '))
cont = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    if cont > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial), end='')



