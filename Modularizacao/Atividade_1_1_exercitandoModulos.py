"""
 Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
 Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
# código principal

import Atividade_1_2

preco = int(input('Digite um preço: '))

print(f'A metade de R$ {preco} é {Atividade_1_2.metade(preco)}')
print(f'O dobro de R$ {preco} é {Atividade_1_2.dobro(preco)}')
print(f'Aumentando 10%, sobre R$ {preco} temos R$ {Atividade_1_2.porcentagem(preco, 10)}')












