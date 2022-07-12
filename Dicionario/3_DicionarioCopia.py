estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())   # Assim que faz cópia de um dicionário para uma lista. O metodo de [:] não funciona.
for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print()