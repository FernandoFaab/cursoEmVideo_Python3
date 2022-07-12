"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando números da lista: ', end='')
    for cont in range(0,5):
        lista.append(randint(1,10))
    for x in numeros:
        print(f'{x} ', end='')
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):

    par = 0
    for x in lista:
        if x % 2 == 0:
            par += x
    print(f'Somando os valores pares de {lista}: ', end='')
    sleep(1)
    print(par)

numeros = list()
sorteia(numeros)
somaPar(numeros)





