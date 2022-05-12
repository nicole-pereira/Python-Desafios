#é mutavel

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

#segundo exemplo
valores = list()
'''valores.append(6)
valores.append(1)
valores.append(4)'''

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

#união de listas
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#cópia de listas
a = [2, 3, 4, 7]
b = a[:]
#cria uma cópia de A entro de B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
