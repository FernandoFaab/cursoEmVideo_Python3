"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
lista = list()
lista2 = list()
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    lista2.append(lista[:])
    lista.clear()
    resposta = input('Deseja continuar? [S/N]: ')
    if resposta in 'Nn':
        break
print('-=' * 15)
print(f'{"nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for cont, x in enumerate(lista2):
    print(f'{cont:<4}{x[0]:<10}{x[1]+x[2]/2:>8.1f}')
while True:
    print('-' * 30)
    resposta2 = int(input('Mostrar notas de qual aluno? [999/FINALIZA]: '))
    if resposta2 == 999:
        print("FINALIZANDO...")
        break
    if resposta2 <= len(lista2) -1:
        print(f'As notas de {lista2[resposta2][0]} são {lista2[resposta2][1:]}')




