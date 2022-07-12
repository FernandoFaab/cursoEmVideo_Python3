"""
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número real: {num}, e o número inteiro {num2}')
