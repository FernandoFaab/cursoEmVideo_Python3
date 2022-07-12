"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep

def valores (* num):
    print('=-' * 30)
    print('Analisando os valores passados...')
    for x in num:
        print(f'{x} ', end='', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi {max(num)}')


valores(1,3,9,5,4,2,3)
valores(65,23,3,54,96,106)
