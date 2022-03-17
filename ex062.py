#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 13)
print('GERADOR DE PA')
print('=' * 13)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeiro
contermo = 0
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} ➔ '.format(termo), end='')
        termo += razao
        cont += 1
        contermo += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados'.format(contermo))

