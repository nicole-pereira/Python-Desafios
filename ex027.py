#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual seu nome? ')).strip()

n = nome.split()
first = n[0]
last = n[len(n)-1]
#o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.

print('Seu primeiro nome é {}\nSeu último nome é {}'.format(first, last))
