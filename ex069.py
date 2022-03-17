#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

countm = countage = countf = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    age = int(input('Idade: '))
    sex = str(input('Sexo: [M/F] '))

    if age >= 18:
        countage += 1
    if sex in 'Ff' and age < 20:
        countf += 1
    if sex in 'Mm':
        countm += 1

    decisao = ' '
    while decisao not in 'SN':
        decisao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if decisao in 'Nn':
            break

print(f'Total de pessoas com mais de 18 anos: {countage}')
print(f'Ao todo temos {countm} homens cadastrados')
print(f'E temos {countf} mulheres com menos de 20 anos')
