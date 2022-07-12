"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
lista = list()
lista2 = list()
maior = menor = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(lista2) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    resposta = input('Quer continuar? [S/N]: ')
    lista2.append(lista[:])
    lista.clear()
    if resposta in 'Nn':
        break
print(lista2)
print('-=' * 30)
print(f'Ao todo você cadastrou {len(lista2)} pessoas.')
print(f'O maior peso foi : {maior}Kg. Peso de ', end='')
for x in lista2:
    if x[1] == maior:
        print(f'[{x[0]}] ', end='')
print()
print(f'O menor peso foi : {menor}Kg. Peso de ', end='')
for x in lista2:
    if x[1] == menor:
        print(f'[{x[0]}] ', end='')
print()



