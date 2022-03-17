#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

linha = '-' * 18
total = count = maior = menor = 0

print(linha)
print('LOJA SUPER BARATÃO')
print(linha)
barato = ' '
while True:
    name = str(input('Nome do Produto: '))
    price = float(input('Preço: R$'))
    count += 1
    total += price

    if price > 1000:
        maior += 1

    if count == 1 or price < menor:
        menor = price
        barato = name

    question = ' '
    while question not in 'SN':
        question = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if question == 'N':
        break

print(linha, end='')
print(' FIM DO PROGRAMA ', end='')
print(linha)

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')
