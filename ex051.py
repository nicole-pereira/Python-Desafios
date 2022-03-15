#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

first = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = first + (10 - 1) * razao

for c in range(first, decimo + razao, razao):
    print(c, end=' ➔ ')
print('Acabou')
