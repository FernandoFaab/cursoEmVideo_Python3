"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista = []
for x in range(0, 5):
    numero = int(input('Digite um valor: '))
    if x == 0 or numero > lista[-1]:  # se for o primeiro coloca sendo o fim, se for o maior, também coloca no fim.
        lista.append(numero)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  # aqui eu criei um código, que ele verifica do primeiro 0 até o ultimo da lista.
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(lista)




