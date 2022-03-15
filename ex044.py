#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros

print('='*7)
print('Lojinha')
print('='*7)

preco = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))


if opcao == 1:
    total = preco - (preco * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preco, total))
elif opcao == 2:
    total = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preco, total))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preco/2))
    print('Sua compra vai custar R${:.2f} no final.'.format(preco))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = preco + (preco * 0.20)
    pjuros = juros/parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, pjuros))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, juros))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente Novamente')
