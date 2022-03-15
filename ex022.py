#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input('Qual é o seu nome? '))

#jeito dele, boa prática
#nome = str(input('Qual é o seu nome? ')).strip()

ma = nome.upper()
mi = nome.lower()

qtdt = ''.join((nome.split()))
qtd = len(qtdt)
"""jeito dele:
(len(nome) - nome.count(' ')))
pq subtrai o que tem de espaço dentro do nome
mto bom.
"""

first = nome.split()
tamfirst = first[0]
qtdfirst = len(first[0])
"""jeito dele:
(nome.find(' '))
nao entendi muito bem mas eh bem mais sucinto
"""

print('Analisando seu nome...\nSeu nome em maiúsculas é {}\nSeu nome em minúsculas é {}\nSeu nome tem ao todo {} letras\nSeu primeiro nome é {} e ele tem {} letras'.format(ma, mi, qtd, tamfirst, qtdfirst))

