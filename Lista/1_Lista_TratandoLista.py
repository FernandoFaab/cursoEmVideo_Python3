"""
lista são elementos semelhantes a tuplas, mas a diferença é que ele pode ser alterado depois de criado.
lista é criado usando colchetes
"""

lista = [1,2,3,4,5]
print(type(lista))

lista.append(6)  # adiciona ao final da lista um item.
print(lista)
lista.insert(2,'Casa')  # adiciona um item a lista, no local que tu queira.
print(lista)
del lista[2]  # Elimina um item a sua escolha da lista.
print(lista)
lista.pop(0)  # se usa com parenteses, elimina o ultimo item da lista. Se você não colocar o item, ele remove o último.
print(lista)
lista.remove(4)  #elimina o item que tu escreveu de forma nomeada.
print(lista)

if 2 in lista:
    lista.remove(2)
print(lista)

print(f'Essa Lista tem {len(lista)} elementos')  # conta quantos itens tem na lista
