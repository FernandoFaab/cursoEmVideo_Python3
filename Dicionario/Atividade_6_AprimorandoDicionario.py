jogador = {}
gols = []
lista = []

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for x in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {x+1}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())

    resposta = str(input('Quer continuar cadastrando jogador? [S/N] ')).upper()[0]
    if resposta == 'S':
        jogador.clear()
        gols.clear()
        continue
    else:
        break

print('-=' * 30)

print(f'{"cod":<4}{"NOME":<10}{"gols":>8}{"Total":>15}')
print('-' * 60)
for x, y in enumerate(lista):
    print(f'{x:>3}', end=' ')
    for d in y.values():
        print(f'{str(d):<15}', end='')
    print()

print('-' * 60)
while True:
    resposta2 = int(input('Mostrar notas de qual jogador? [999/FINALIZA]: '))
    if resposta2 == 999:
        print("FINALIZANDO...")
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[resposta2]["nome"]}')
        for x, y in enumerate(lista[resposta2]["gols"]):
            print(f'   No jogo {x+1} fez {y} gols')
    print("-" * 60)

