'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

lista = []
pessoas = {}
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    while sexo not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoas['sexo'] = sexo

    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']

    lista.append(pessoas.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
        break

media = soma / len(lista)

print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print('\nD) Lista das pessoas que estão acima da média: ', end='')
for l in lista:
    if l['idade'] >= media:
        print('   ', end='')
        for k, v in l.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n<<<ENCERRADO>>>')
