print('-' * 30)
print('ROLE PLAY GAME')
print('-' * 30)

while True:
    dados = int(input('Qual tipo de dado desejas rolar? D-'))
    quantidade = int(input('Quantos dados serão rolados? '))

    lista = list()

    for x in range(0, quantidade):
        import random
        numero = random.randint(1, dados)
        lista.append(numero)

    print(lista)

    pergunta = input('Deseja continuar rolando? [S/N]: ')
    if pergunta in 'Nn':
        break
    else:
        print('-' * 30)
        continue





