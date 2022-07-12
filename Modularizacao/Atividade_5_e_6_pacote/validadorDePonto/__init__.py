"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':  # verifica se é letra ou se está vazio, para dar erro.
            print(f'\033[0;31mERRO: \"{entrada}\" é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)
