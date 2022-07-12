"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
"""
def ficha(x = '<DESCONHECIDO>', y=  0):
    print(f'O jogador {x}, fez {y} gols(s) no campeonato')


nome = str(input("Nome do jogador: "))
gols = str(input("Quantos gols ele fez: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(y=gols)
else:
    ficha(nome, gols)
