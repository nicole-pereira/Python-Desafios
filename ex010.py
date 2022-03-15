#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.s

din = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = din/5.03

print('Com {:.2f} você pode comprar U${:.2f}.' .format(din, dol))

