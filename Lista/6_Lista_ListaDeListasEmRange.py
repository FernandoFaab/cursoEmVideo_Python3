galera = list()
dado = list()
for x in range(0,3):  # criando um contagem de 0 a 3
    dado.append(str(input('Digite o nome: ')))  # inserindo nome na lista dado
    dado.append(int(input('Digite a idade: ')))  # inserindo idade na lista dado
    galera.append(dado[:])  # fazendo uma cópia da lista dado dentro da lista galera
    dado.clear()  # apagando a lista dado.

print(dado)
print(galera)

print('-=' * 30)

maior = menor = 0
for x in galera:
    if x[1] >= 18:
        print(f'{x[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{x[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maior de idade e {menor} de idade.')