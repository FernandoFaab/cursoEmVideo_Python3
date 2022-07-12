"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = (str(input('Quer continuar digitando? [S/N]: ')))
    if resposta in 'Ss':
        continue
    else:
        break
par = []
impar = []
for x in lista:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(f'Sua lista foi: {lista}')
print(f'Os números pares digitados foram: {par}')
print(f'Os impares digitados foram: {impar}')
