#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver a sua tabuada: '))
for nc in range(0, 11):
    valor = num * nc
    print('{} x {:2} = {}'.format(num, nc, valor))
