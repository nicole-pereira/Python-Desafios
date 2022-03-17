#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

decisao = 'S'
count = soma = num = maior = menor = 0

while decisao in 'Ss':
    num = int(input('Digite um número: '))
    decisao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma/count
print('Você digitou {} números e a média foi {:.2f}'.format(count, media))

print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


