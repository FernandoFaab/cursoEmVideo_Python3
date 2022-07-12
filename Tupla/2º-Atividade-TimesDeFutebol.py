"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = (
'Corinthians', 'Bragantino', 'Atlético-MG', 'Coritiba', 'São Paulo', 'Santos', 'Cuiabá', 'Internacional', 'Avaí',
'América-MG', 'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará', 'Athletico-PR', 'Atlético Goianiense',
'Goiás', 'Juventude', 'Fortaleza'
)

print('Os 5 primeiros colocados são:', times[0:5])
print('Os 4 últimos são:', times[-4:])
print(f'Os times em ordem alfabética são: {sorted(times)}')  # sorted coloca em ordem alfabética, sem precisar da list
print(f'Flamengo está na {times.index("Flamengo")+1}º posição.')  # o index enumera o item da tupla.

"""
alfabetica = list(times)
alfabetica.sort()
print('Os times em ordem alfabética são: ', alfabetica)
"""

"""
for x, y in enumerate(times):
    if y == 'Flamengo':
        print(f'Flamengo está na {x+1}º posição.')
"""



