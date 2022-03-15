#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#pega o comprimento do junto e diminui um pois ele vai de 19 a 0 e não de 20 a 1
#segundo -1 pois a primeira letra é 0
#o último -1 é pq ele vai voltar, nao seguir em frente
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
