#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

age = 0
mediage = 0
velho = 0
nomevelho = ''
mav = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    age += idade

    if p == 1 and sexo in 'Mm':
        velho == idade
        nomevelho = nome
    if idade > velho and sexo in 'Mm':
            velho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
            mav += 1

mediage = age/4
print('A média de idade do grupo é de {}'.format(mediage))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mav))




