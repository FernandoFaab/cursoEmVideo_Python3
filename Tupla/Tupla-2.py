"""
Tuplas são listas imutaveis, que ficam entre parenteses.
Você não pode deletar itens da tupla.
"""

a = (2,5,4)
b = (5,8,1,2)

c = a + b  # junta as tuplas, na ordem da operação.
d = b + a  # junta as tuplas, na ordem da operação.

print(c)
print(d)
print(c.count(5))  # vai contar quantas vezes aparece o número 5 na tupla C
print(c.index(8))  # diz qual a posição do elemento pedido. Lembrando que ele acha a primeira ocorrência.
print(c.index(2, 2))  # aqui ele procura o elemento, mas a partir da posição dois, pulando a posição 0 e 1.
