#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

resposta = ''
valores = []
while resposta in 'sS':
    valor = int(input('Digite um valor: '))

    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(valor)

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

print('-='*20)
valores.sort()
print(f'Você digitou os valores {valores}')
