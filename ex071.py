#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

linha = '=' * 30
print(linha)
print('{:^30}'.format('BANCO CEV'))
print(linha)

value = int(input('Qual valor você quer sacar? R$'))

total = value
ced = 50
totced = 0

while True:

    if total >= ced:
        total -= ced
        totced += 1

    else:
        print(f'O total de cédulas de {ced} é {totced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            ced = 0

        elif total == 0:
            break


print(linha)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
