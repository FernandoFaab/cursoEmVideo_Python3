""" Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. """
print('-' * 30)
print('GERADOR DE JOGOS DA MEGA SENA')
print('-' * 30)

jogos = int(input('Quantos jogos você quer gerar? '))
lista = list()
lista2 = list()

from time import sleep

for x in range(0, jogos):
    while True:
        if len(lista) != 6:
            import random
            numero = random.randint(1, 60)
            if numero not in lista:
                lista.append(numero)
        else:
            lista2.append(lista[:])
            lista.clear()
            break
sleep(2)
print('-=' *3, f'SORTEANDO {jogos} JOGOS', '-=' * 3)
print()

sleep(2)
for cont, x in enumerate(lista2):
    print(f'Jogo {cont+1}: {sorted(x)}')
    sleep(2)

print()
print('-=' *3, f'BOA SORTE', '-=' * 3)


