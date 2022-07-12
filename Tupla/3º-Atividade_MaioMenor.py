"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint
tupla = tuple(randint(i + 0,9) for i in range(randint(5,5)))

for x in tupla:
    print(f'{x} ', end='')
print()
print(f'O maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')
