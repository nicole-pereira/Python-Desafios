for c in range(1, 8):
    print(c)
print('FIM')
####################################
for c in range(1, 8, 2):
    print(c)
####################################
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
#####################################3
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
##########################
#fica repetindo a mensagem de dentro do for
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('fim')
#############################
s=0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #s recebe s + n
print('O somatório de todos os valores foi {}'.format(s))
