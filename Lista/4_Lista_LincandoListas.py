"""quando você faz copia de lista usando = as listas ficam lincadas. O que tu muda em um muda no outro."""

a = [1,2,3,4,5]
b = a
print(f'Mostrando lista {a}')
print(f'mostrando lista {b}')
b.append(6)
print(f'Mostrando lista {a}')
print(f'mostrando lista {b}')

c = a[:]  # colocar cochetes com dois pontos, faz uma copia dos itens da lista,na nova lista.
c.pop(0)
print(f'mostrando lista {c}')  # verá que a c tem mudança, porque ela é uma cópia.
print(f'mostrando lista {a}')  # verá que a lista 'a' não teve mudança, porque foi mudado apenas a C