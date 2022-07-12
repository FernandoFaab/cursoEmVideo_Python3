"""
tupla, são listas imutaveis
"""
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[1:3])  # nesta regra ele desconsidera o último.
print(lanche[:2])
print(lanche[-1])  # mostra de trás para frente.
print()

for x in lanche:  # se não precisar de posição, apenas a lista/tupla
    print(f'Eu vou comer {x}; ')
print('pra caramba')
print()

for cont in range(0, len(lanche)):  # se precisar da posição
    print(lanche[cont])
print()

for c, y in enumerate(lanche):  # se precisar do elemento e da posição
    print(f'Eu vou comer {y} {c + 1}º ')
