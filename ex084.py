#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dado = list()
pessoa = list()
pesado = leve = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    if len(pessoa) == 0:
        pesado = leve = dado[1]
    else:
        if dado[1] > pesado:
            pesado = dado[1]
        if dado[1] < leve:
            leve = dado[1]

    pessoa.append(dado[:])
    dado.clear()

    resp = str(input(('Quer continuar? [S/N] '))).strip().upper()[0]
    if resp in 'Nn':
        break

print('-='*30)
#não preciso fazer o contador, posso usar o len
print(f'Ao todo, você cadastrou {len(pessoa)} pessoas')
print(f'O maior peso foi de {pesado}Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == pesado:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {leve}Kg. Peso de ', end='')
for p in pessoa:
    if p[1] == leve:
        print(f'[{p[0]}]')
