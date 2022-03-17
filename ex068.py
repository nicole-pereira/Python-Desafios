#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

computador = randint(1, 10)
count = num = 0

while True:
    print('-=' * 12)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-=' * 12)
    num = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper()[0]
    print('-' * 20)

    total = num + computador
    print(f'Você jogou {num} e o computador {computador}. Total de {total}')
    print('-' * 20)

    resto = total % 2

    if resto == 0:
        print('DEU PAR!')
        if escolha == 'P':
            print('Você Venceu!\nVamos jogar novamente...')
            count += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif resto != 0:
        print('DEU ÍMPAR!')
        if escolha == 'I':
            print('Você Venceu!\nVamos jogar novamente...')
            count += 1
        else:
            print('VOCÊ PERDEU')
            break

print(f'GAME OVER! Você venceu {count} vezes.')

