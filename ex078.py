#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valor = []
maior = menor = 0
for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {cont}: ')))

    if cont == 0:
        maior = menor = valor[cont]
    else:
        if valor[cont] > maior:
            maior = valor[cont]
        elif valor[cont] < menor:
            menor = valor[cont]

print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO maior menor digitado foi {menor} nas posições: ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}...', end='')



