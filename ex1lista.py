lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
par = impar = 0

print('Números pares: ', end='')

for i in lista:
    if i % 2 == 0:
        print(f' {i} ', end='')
print('\nNúmeros impares: ', end='')
for i in lista:
    if i % 2 != 0:
        print(f' {i} ', end='')
print('\nMúltiplos de 2, 3 e 4: ', end='')
for i in lista:
    if i % 2 == 0 or i % 3 == 0 or i % 4 == 0:
        print(f' {i} ', end='')

print(f'\nIntervalo de 1 a 9: {lista[1:10]}')
print(f'Intervalo de 8 a 13: {lista[8:14]}')
lista.reverse()
print(f'Lista reversa: {lista}')
