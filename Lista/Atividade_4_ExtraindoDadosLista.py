"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = (str(input('Quer continuar digitando? [S/N]: ')))
    if resposta == 's':
        continue
    else:
        break

print(f'Sua lista possui {len(lista)} números.')
lista.sort(reverse = True)
print(lista)
if 5 in lista:
    print('O número 5 está em sua lista')
else:
    print('O número 5 não está em sua lista')
