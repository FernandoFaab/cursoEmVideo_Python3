jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
for x in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {x+1}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for x, y in jogador.items():
    print(f'O campo {x} tem o valor {y}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'   => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {sum(jogador["gols"])}')

