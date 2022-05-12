'''Exercício Python 101:
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc

    print(f'Com {idade} anos: VOTO ', end='')
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATORIO'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
