""" Criando listas  """

lista = list(range(4,11))  # cria lista atraves de um range/intervalo de números pré escolhidos.
print(lista)

lista2 = list(range(4,11,2))  # cria lista atraves de um range/intervalo e pulando de 2x2
print(lista2)

lista3 = [4,6,2,8,7,3]  # criando lista de forma tradicional.
lista3.sort()  # este comando organiza uma lista de forma crescente.
print(lista3)
lista3.sort(reverse=True)  # aqui você coloca a lista de forma descrescente
print(lista3)

for x, y in enumerate(lista3):  # o enumerate, serve para tu enumerar a lista. O primeiro parametro do for sera o núm
    print(f'Na posição{x} encontrei o valor {y}')



