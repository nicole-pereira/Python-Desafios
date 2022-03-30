#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
#guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

aluno = {}
situ = []

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
'''
situ.append(aluno.copy())

print(f'- Nome é igual a {aluno["nome"]}')
print(f'- A média é igual a {aluno["media"]}')

print(f'- A situação é igual a ', end='')
if aluno['media'] >= 7:
    print('Aprovado!')
elif 5 <= aluno['media'] < 7:
    print('Recuperação')
else:
    print('Reprovado')
'''
#jeito dele
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')


