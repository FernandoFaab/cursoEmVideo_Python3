"""
Crie um pacote chamado Atividade_5 que tenha dois módulos internos chamados códigos e ???.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""

"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""
from Modularizacao.Atividade_5_e_6_pacote import códigos
from Modularizacao.Atividade_5_e_6_pacote import validadorDePonto

preco = validadorDePonto.leiaDinheiro('Digite o preço: R$ ')
códigos.resumo(preco)

