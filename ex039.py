#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year

ano = int(input('Ano de nascimento: '))
idade = atual - ano

print('Quem nasceu em {} tem {} anos em 2022'.format(ano, idade))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    anos = 18 - idade
    aano = atual + anos
    print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}'.format(anos, aano))

elif idade > 18:
    anos = idade - 18
    aano = atual - anos
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(anos, aano))


