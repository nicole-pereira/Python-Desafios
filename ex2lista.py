#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

lista = []

for c in range(0, 5):
    lista.append((int(input('Digite um número: '))))
print(list(enumerate(lista)))
