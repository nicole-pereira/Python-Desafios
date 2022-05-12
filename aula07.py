'''
#em relação a alinhamento

nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))

#20 caracteres
print('Prazer em te conhecer, {:20}!'.format(nome))

#20 caracteres a direita
print('Prazer em te conhecer, {:>20}!'.format(nome))

#20 caracteres a esquerda
print('Prazer em te conhecer, {:<20}!'.format(nome))

#20 caracteres centralizado
print('Prazer em te conhecer, {:20}!'.format(nome))

'''

n1 = int(input("Um numero: "))
n2 = int(input('Outro  numero: '))

sum = n1+n2
sub = n1-n2
multi = n1*n2
div = n1/n2
pot = n1**n2
divsr = n1//n2
rest = n1%n2

#:.3f limita o float a 3 casas
print('A soma entre {} e {} é: {}, a subtração é: {}, a multiplicação é: {}, a divisão é: {:.3f}' .format(n1, n2, sum, sub, multi, div))
print('A potencia é: {}, a divisão sem resto é: {} e o resto da divisão é: {}' .format(pot, divsr, rest))



