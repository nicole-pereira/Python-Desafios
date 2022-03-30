#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    lista.append(num)

    if num % 2 == 0:
        par.append(num)
    elif num % 2 != 0:
        impar.append(num)

    if resp in 'Nn':
        break

print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
