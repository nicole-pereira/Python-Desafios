#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

pessoas = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    pessoas.append([nome, [nota1, nota2], media])

    if resp in 'Nn':
        break
print('-='*25)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":<8}')
print('-'*25)
for i, p in enumerate(pessoas):
    print(f'{i:<4} {p[0]:<10} {p[2]:<8}')

while True:
    print('-='*25)
    aluno = int(input('Mostrar notas de qual aluno? [999 interrompe] '))

    for i, p in enumerate(pessoas):
        if aluno == i:
            print(f'As notas de {p[0]} são {[p[1]]}')

    if aluno == 999:
        break

