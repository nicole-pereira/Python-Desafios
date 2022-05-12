#Tuplas

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#os três resultam na mesma coisa

#se eu não precisar da posição
for comida in lanche:
    print(f'Eu vou comer {comida}')

#usado quando quer saber a posição (cont)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#o mesmo de cima śo que pra saber a pocição
#precisa por duas variaveis no for
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi para caramba!')


print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
#quando usa + em tupla, ela junta as duas
c = a + b
#tamanho da dupla
print(len(c))
#contar quantos 5 tem na tupla
print(c.count(5))
#A posição que o numero se encontra
print(c)
print(c.index(8))



pessoa = ('Gustavo', 39, 'M', 99.88)
#apaga tupla
del(pessoa)
print(pessoa)
#Não posso deletar um item na tupla, mas eu posso deletar a tupla inteira
