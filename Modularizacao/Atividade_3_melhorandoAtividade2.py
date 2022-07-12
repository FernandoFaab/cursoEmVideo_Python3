"""
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 2.
"""

"""
Aqui eu vou criar no código da Atividade_1_2 um código, que puxa a formatação se eu acrescentar o parâmetro True
"""

import Atividade_1_2

preco = int(input('Digite um preço: '))

print(f'A metade de {Atividade_1_2.moeda(preco)} é {Atividade_1_2.metade(preco, True)}')
print(f'O dobro de {Atividade_1_2.moeda(preco)} é {Atividade_1_2.dobro(preco, True)}')
print(f'10%, sobre {Atividade_1_2.moeda(preco)} temos R$ {Atividade_1_2.porcentagem(preco, 10, True)}')
