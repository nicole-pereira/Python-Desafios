#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2

print('A média entre as notas {:.1f} e {:.1f} é {:.1f}' .format(n1, n2, m))
#ele faz o arredondamento!! mto legal


