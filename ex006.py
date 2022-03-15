#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))

dob = num * 2
tri = num * 3
rq = num ** (1/2)

print('O dobro de {} vale {} \nO triplo de {} vale {} \nA raiz quadrada de {} é {:.3f}' .format(num, dob, num, tri, num, rq))
