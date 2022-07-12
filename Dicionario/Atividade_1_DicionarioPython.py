"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""
programa = dict()
programa['nome'] = str(input("nome: "))
programa['media'] = float(input(f'Média de {programa["nome"]}: '))
if programa['media'] >= 7.0:
    programa['situacao'] = 'APROVADO'
elif (programa['media'] > 3.0) and (programa['media'] < 7.0):
    programa['situacao'] = 'RECUPERAÇÃO'
else:
    programa['situacao'] = 'REPROVADO'

print('-=' * 30)

"""
K será keys, e V será valores. Em dicionario não tem enumerate. Como coloquei .items, ele vai ler keys e valores. 
se fosse .kays, seria só valor. Se fosse .values seria só os valores. 
"""
for k, v in programa.items():
    print(f' - {k} é igual a {v}')




