"""
Exercício Python 107:
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from ex108 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formato(valor)} é {moeda.formato(moeda.metade(valor))}')
print(f'O dobro de {moeda.formato(valor)} é {moeda.formato(moeda.dobro(valor))}')
print(f'Aumentando 10%, temos {moeda.formato(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 20%, temos {moeda.formato(moeda.diminuir(valor, 20))}')
