"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
lista = list()
lista2 = list()
par = list()
coluna3 = list()
for x in range(0, 3):
    for y in range(0, 3):
        numero = int(input(f'Digite um valor para [{x}, {y}]: '))
        lista.append(numero)
    lista2.append(lista[:])
    lista.clear()
print('-=' * 30)
for x in lista2:
    for cont, y in enumerate(x):
        if y % 2 == 0:
            par.append(y)
        if cont == 2:
            coluna3.append(y)
        print(f'[{y:^5}]', end='')
    print()
print('-=' * 30)
print(f"A soma dos pares é: {sum(par)}")   # sum faz soma dos itens da lista.
print(f'A soma da 3º coluna é: {sum(coluna3)}')
print(f'O maior valor da linha 2 é: {(max(lista2[1]))}')
