#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[1] converter para BINARIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

bin = bin(num)
oct = oct(num)
hex = hex(num)

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex[2:]))
