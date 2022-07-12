"""
 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
 separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]
for x in range(0,7):
    numero = int(input(f'Digite o {x+1}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

print('-=' * 30)

lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')











