teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

pessoal = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoal[3][0])

for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade.')

gente = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
#muito importante não esquecer do [:] para copiar uma lista
    gente.append(dado[:])
    dado.clear()

for g in gente:
    if g[1] >= 18:
        print(f'{g[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{g[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade')
