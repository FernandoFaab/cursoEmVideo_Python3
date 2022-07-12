"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""
jogadas = {}

import random
jogadas['jogador1'] = random.randint(1, 6)
jogadas['jogador2'] = random.randint(1, 6)
jogadas['jogador3'] = random.randint(1, 6)
jogadas['jogador4'] = random.randint(1, 6)

from time import sleep
for x, y in jogadas.items():
    sleep(2)
    print(f'{x} tirou {y}')

sleep(2)
print('-=' * 15)
print(' == RANKING DOS JOGADORES == ')

ranking = 1
for i in sorted(jogadas, key=jogadas.get, reverse=True):
    print(f' {ranking}º lugar: {i} tirou {jogadas[i]}')
    ranking += 1
    sleep(2)










