"""
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de
tinta pinta uma área de 2 metros quadrados.
"""

larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))

area = larg*altu
litro = area/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, altu, area))
print('Para pintar sua parede, você precisará de {}l de tinta.'.format(litro))
