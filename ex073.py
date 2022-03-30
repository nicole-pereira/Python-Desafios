#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

linha = ('=-' * 20)
times = ('Flamengo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', "Athletico Paranaense",
         'Santos', 'São Paulo', 'Internacional', 'Fluminense', 'Corinthians', 'Fortaleza',
         'Bahia', 'Ceará', 'Cruzeiro', 'América Mineiro', 'Atlético Goianiense', 'Chapecoense',
         'Botafogo', 'Vasco da Gama', 'Red Bull Bragantino')

print(linha)
print(f'Lista de times do Brasileirão: {times}')
print(linha)
print(f'Os 5 primeiros são: {times[0:5]}')
print(linha)
print(f'Os 4 últimos são: {times[-4:]}')
print(linha)
print(f'Times em ordem alfabética: {sorted(times)}')
print(linha)
print(f'O Chapecoense está na {times.index("Chapecoense")}ª posição')
