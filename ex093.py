'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
qtdGol = []

jogador['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, partidas):
     qtdGol.append(int(input(f'  Quantos gols jogou na partida {c+1}? ')))

#nao pode esquecer o [:]
jogador['gols'] = qtdGol[:]
jogador['total'] = sum(qtdGol)
linha = '-=' * 30
print(linha)
print(jogador)
print(linha)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(linha)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    if v == 1:
        print(f'    => Na partida {i+1}, fez {v} gol.')
    else:
        print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Fez um total de {jogador["total"]} gols.')
