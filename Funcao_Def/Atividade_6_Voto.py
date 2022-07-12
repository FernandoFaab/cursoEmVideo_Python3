"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(ano):
    from datetime import date  # esta função importa data.
    atual = date.today().year  # esta função seleciona o ano atual.
    idade = atual - ano

    if idade < 16:
        return f'com {idade}: VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade}: VOTO OPCIONAL!'
    else:
        return f'com {idade}: VOTO OBRIGATORIO!'

nascimento = (int(input("Em que ano você nasceu? ")))
print(voto(nascimento))  # aqui eu jogo a input nascimento, dentro de voto.