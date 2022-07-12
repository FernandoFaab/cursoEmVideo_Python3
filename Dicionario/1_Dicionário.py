"""
Os dicionários são identificados com {} chaves.
A forma de criar um dicionário é: dado = dict() ou dado = {}
"""
# Neste exemplo, eu criei duas chaves. Uma nome com o dado pedro, e uma idade com o dado 25.
dado = {'nome': 'pedro', 'idade': 25}
print(dado['nome'])  # ou seja, eu peço a impressão da chave, e recebo o valor dela.
# Não se da APPEND em dicionário. Você apenas declara uma nova chave, com o seu valor. Ela vai para o final do dict.
dado['sexo'] = 'm'
print(dado)
del dado['idade']  # É com del que se deleta um item do dicionário. Mas você deleta a chave, o valor vai junto.
print()

# Exemplo de criação de dicionário:

filme = {'titulo': 'Star Wars', 'ano': 1917, 'diretor': 'George Lucas'}
print(filme)
print(filme['ano'])  # Aqui eu printo só o valor que está contido na chave ano.
print(filme.values())  # aqui ele vai imprimir todos os valores contidos no meu dicionario.
print(filme.keys())  # aqui eu imprimo todas as chaves, ou seja os titulos de cada valor.
print(filme.items())  # aqui voccê imprime tudo, chave e valor.
print()

for k, v in filme.items():  # aqui eu crio um for, para rodar na chave e no valor dela. NÃO TEM ENUMERETE, tem o itens.
    print(f'O {k} é {v}')  # aqui eu imprimo a chave e o valor.
