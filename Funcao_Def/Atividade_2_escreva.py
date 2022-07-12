"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
"""

def mensagem (msg):
    tamanho = len(frase)
    print('~' * tamanho)
    print(msg)
    print('~' * tamanho)


while True:
    frase = input()
    mensagem(frase)
    if frase == "fim":
        break
