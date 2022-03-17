#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

opcao = 0

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

while opcao != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    print('-='*15)
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(num1, num2, (num1 + num2)))
        sleep(0.7)
    elif opcao == 2:
        print('A multiplicação entre {} x {} é {}'.format(num1, num2, (num1*num2)))
        sleep(0.7)
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        elif num1 < num2:
            maior = num2
        else:
            print('Os números são iguais')
        print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior))
        sleep(0.7)
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        sleep(0.5)
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
print('-='*15)
sleep(0.7)
print('Fim do programa! Volte sempre!')

