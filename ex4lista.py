#Ler uma lista com 4 notas, em seguida
#o programa deve exibir as notas e a média.

lista = []

for c in range(0, 4):
    lista.append(float(input('Digite uma nota: ')))

med = (sum(lista))/4
print(f'Notas: {lista}\n Média: {med}')
