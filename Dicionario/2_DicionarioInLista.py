filme1 = {'titulo': 'Star Wars', 'ano': 1917, 'diretor': 'George Lucas'}
filme2 = {'titulo': 'Avenges', 'ano': 2012, 'diretor': 'Joss Whedon'}
lista = [filme1, filme2]
print(lista)
print(lista[0])  # aqui vai printar o primeiro dicionário inteiro da lista. 
print(lista[0]['ano'])  # desta forma eu acesso a lista 0 que contem o dicionário filme1. Ai depois eu acesso o ano.
print(lista[1]['diretor'])  # acesso a lista 1 que tem o dicionario filme2, e depois acesso a chave diretor.
