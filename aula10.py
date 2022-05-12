#primeiro

nome = str(input('Qual seu nome? '))
if nome == 'Nicole':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia {}!' .format(nome))


#segundo
n1 = float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))

n=(n1+n2)/2

print('Sua média foi: {}' .format(n))
if n >= 6.5:
    print('Você passou!')
else:
    print('Reprovou')
