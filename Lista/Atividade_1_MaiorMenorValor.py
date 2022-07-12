"""
ATIVIDADE
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
menor = 0
maior = 0
for x in range(0,5):
    lista.append(int(input(f'Digite o {x+1}º dos seus 5 números: ')))

    if x == 0:
        menor = maior = lista[x]
    else:
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < lista[x]:
            menor = lista[x]

print('-=' * 30)
print(f'Esta é sua lista {lista}')
print(f'O maior valor da lista é {maior}, nas posições: ', end='')
for x, y in enumerate(lista):
    if y == maior:
        print(f'{x},', end='')
print(f'\nO menor valor dela é {menor}, nas posições: ', end='')
for x, y in enumerate(lista):
    if y == menor:
        print(f'{x},', end='')


"""
print(f'O maior valor dela é {max(lista)}')  # Jeito mais fácil de achar o maior
print(f'O menor valor dela é {min(lista)}')  # Jeito mais fácil de achar o menor
"""