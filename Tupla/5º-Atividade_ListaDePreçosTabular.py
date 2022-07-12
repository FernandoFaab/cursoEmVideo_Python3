"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = (
    'lapis', 1.25,
    'caderno', 10.35,
    'borracha', 2.5,
    'caneta', 1.50,
    'tinta', 5.75

)

print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)

for x in range (0, len(listagem)):
    if x % 2 ==0:
        print(f'{listagem[x]:.<30}', end='')
    else:
        print(f'RS{listagem[x]:>7.2f}')
