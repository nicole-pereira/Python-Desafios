'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
 Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
 Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date
pessoa = {}
anoAtual = date.today().year

pessoa['nome'] = str(input('Nome: '))

nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = anoAtual - nascimento

pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['anoContrat'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['anoContrat'] + 35) - anoAtual)

print('-='*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')

