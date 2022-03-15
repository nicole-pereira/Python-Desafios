#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}.'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif 25 >= imc >= 18.5:
    print('Peso Ideal')
elif 30 >= imc > 25:
    print('Sobrepeso')
elif 40 >= imc > 30:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')
