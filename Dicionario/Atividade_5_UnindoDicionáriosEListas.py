"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
lista = list()
cadastros = dict()
soma = 0

while True:
    cadastros['nome'] = str(input('Nome: '))
    while True:
        cadastros['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if cadastros['sexo'] in 'FfMm':
            break
        else:
            print('ERRO! por favor, digite apenas M ou F.')
            continue
    cadastros['idade'] = int(input('Idade: '))
    soma = soma + cadastros['idade']
    lista.append(cadastros.copy())
    cadastros.clear()

    while True:
        continuar = input('Deseja continuar? [S/N] ').upper()[0]
        if continuar in 'SsNn':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if continuar in 'Ss':
        continue
    if continuar in 'Nn':
        break
print('-=' * 30)

print(f'A) Ao todo temos {len(lista)} cadastradas')
print(f'B) A média das idades é de {soma/len(lista):5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for x in lista:
    if x['sexo'] in 'Ff':
        print(f'{x["nome"]}; ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for x in lista:
    if x['idade'] > soma/len(lista):
        print(f'   Nome = {x["nome"]}; sexo = {x["sexo"]}, Idade = {x["idade"]};')





