"""
Adapte o código do desafio 1, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""

import Atividade_1_2

preco = int(input('Digite um preço: '))

print(f'A metade de {Atividade_1_2.moeda(preco)} é {Atividade_1_2.moeda(Atividade_1_2.metade(preco))}')
print(f'O dobro de {Atividade_1_2.moeda(preco)} é {Atividade_1_2.moeda(Atividade_1_2.dobro(preco))}')
print(f'10%, sobre {Atividade_1_2.moeda(preco)} temos R$ {Atividade_1_2.moeda(Atividade_1_2.porcentagem(preco, 10))}')
