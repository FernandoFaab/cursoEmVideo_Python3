"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
lista = []
expressao = (input("digite sua expressão númerica: "))

for x in expressao:
    lista.append(x)

abertos = lista.count('(')
fechados = lista.count(')')

if abertos == fechados:
    print('Sua expressão númerica é valida')
else:
    print('Sua expressão númerica é invalida')

