'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = []
jogador = {}
qtdGol = [] #partidas

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, partidas):
        qtdGol.append(int(input(f'  Quantos gols na partida {c+1}? ')))

    jogador['gols'] = qtdGol[:]
    jogador['total'] = sum(qtdGol)
    qtdGol.clear()

    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'Nn':
            break

print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    print('-' * 40)
    dados = int(input('Quer ver os dados de qual jogador? [999 interrompe] '))

    if dados == 999:
        break

    if dados >= len(time):
            print(f'ERRO! Não existe jogador com o código {dados}')

    for i, p in enumerate(time):
        if dados == i:
            print(f'--- Levantamento do jogador {p["nome"]}')
            for j, v in enumerate(p['gols']):
                print(f'No jogo {j+1} fez {v} gols')

print('<<<ENCERRADO>>>')
