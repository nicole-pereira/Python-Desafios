#Ler um vetor com 20 idades e exibir a maior e menor.

lista = []
maior = menor = 0

for v in range(0, 20):
    lista.append(int(input(f'Digite o {v}º número: ')))

    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        elif lista[v] < menor:
            menor = lista[v]

print(f'Números: {lista}')
print(f'Menor: {menor}')
print(f'Maior: {maior}')
