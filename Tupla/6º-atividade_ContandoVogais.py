"""
 Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
 para cada palavra, quais são as suas vogais.
"""

palavras = ('fernando', 'augusto', 'alves', 'batista')

for x in palavras:
    print(f'\nNa palavra {x} temos ', end='')  # o \n é para quebrar linha em cada inicio.
    for letra in x:
        if letra.lower() in 'aeiou':  # o .lower() é para pegar as letras e transformar em minusculas.
            print(letra, end=' ')


