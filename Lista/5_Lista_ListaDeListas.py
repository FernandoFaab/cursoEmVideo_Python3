dados = ['fernando', 31]

pessoas = list()  #  você pode criar lista de dois jeitos, do jeito acima, e deste jeito.
pessoas.append(dados[:])  # aqui eu copiei uma lista inteira, dentro de outra lista.
print(pessoas)  # aqui você pode observar a criação de uma lista de lsitas. Uma lista dentro de uma lista.
print('-=' * 30)

lista =[['fernando', 31],['tayla', 25],['rodrigo', 10]]

print(lista[1])  # se eu não especificar o item da lista, vai ser impresso a lista inteira.
print(lista[0][0])  # aqui eu imprimi a item 0 da lista 0
print(lista[1][1])  # aqui ele vai acessar o item 1 da lista 1
print('-=' * 30)

for x in lista:  # aqui vai imprimir todas as litas, dentro de lista, só que separadamente.
    print(x)
print('-=' * 30)
for x in lista:  # aqui vai imprimir todas os nomes da lista, separadamente.
    print(x[0])
print('-=' * 30)
for x in lista:  # aqui vai imprimir todas as idades da lista, separadamente.
    print(x[1])
print('-=' * 30)
for x in lista:
    print(f'{x[0]} tem {x[1]} anos de idade.')