#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.


while True:
    print('-' * 33)
    num = int(input(('Quer ver a tabuada de qual valor? ')))
    print('-' * 33)
    if num < 0:
        break
    for c in range(1, 11):
        c += 1
        print(f'{num} x {c} = {num * c}')
print('PROGRAMA TABUADA ENCERRADO')
