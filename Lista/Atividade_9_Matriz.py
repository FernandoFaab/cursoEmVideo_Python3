lista = list()
lista2 = list()

for x in range(0, 3):
    for y in range(0, 3):
        numero = int(input(f'Digite um valor para [{x}, {y}]: '))
        lista.append(numero)
    lista2.append(lista[:])
    lista.clear()

print('-=' * 30)
for x in lista2:
    for y in x:
        print(f'[{y:^5}]', end='')
    print()


