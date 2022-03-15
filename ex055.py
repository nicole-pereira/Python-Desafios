#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pmaior = 0
pmenor = 0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso

print('O maior peso lido foi de {}kg'.format(pmaior))
print('O menor peso lido foi de {}kg'.format(pmenor))
