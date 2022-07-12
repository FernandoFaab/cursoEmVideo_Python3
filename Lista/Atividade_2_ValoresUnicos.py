"""
 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
 em ordem crescente.
"""

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = (str(input('Quer continuar digitando? [S/N]: ')))
    if resposta == 's':
        continue
    else:
        break
lista = set(lista)
lista = list(lista)
lista.sort()
print(lista)

# Solução do professor -----------------

lista2 = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista2:
        lista2.append(n)
        print('Número adicionado')
    r = str(input('Quer continuar digitando? [S/N]? '))
    if r in 'Nn':
        break
lista2.sort()
print(lista2)
