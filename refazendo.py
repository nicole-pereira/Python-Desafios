#Exercício Python 087


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = sc = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite para a posição [{l}][{c}]: '))
        matriz[l][c] = num

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
    print()

for l in range(0, 3):
        sc += matriz[l][2]
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]

print(sp)
print(sc)
print(maior)

