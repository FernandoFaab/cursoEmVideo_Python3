"""
docstring é a documentação que você faz do seu DEF. É a explicação que você cria da função que você criou.
Para se alguma pessoa estiver usando ou lendo o seu código. Nela você cria uma explicação, logo abaixo do def,
usando aspas duplas, três vezes de forma identada. Nesta explicação você explica o seu def.
"""

def contador(i,f,p):
    """
    -- programa para contar de i até f, pulando de p em p.
    :param i: inicio da contagem.
    :param f: fim da contagem.
    :param p: passo da contagem.
    :return: sem retrono

    função criada por Fernando Augusto
    """

    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

# assim se você digitar a função interactive help, você recebera a explicação no console.

help(contador)

