"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Seus números são: {tupla}')

print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu {tupla.index(3)+1}ª posição.')
else:
    print('Não há o valor 3.')
print(f'Os números pares digitados são: ', end='')
for x in tupla:
    if x % 2 == 0:
        print(x, end=' ')



