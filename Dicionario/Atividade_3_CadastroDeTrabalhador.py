cadastro = {}
from datetime import datetime

cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nascimento  # pego o ano atual e diminuo com nascimento(Que não ta no dict)
cadastro['clt'] = int(input('Nº da carteira de trabalho [0 não tem]: '))
if cadastro['clt'] == 0:
    print('-=' * 30)
    for x, y in cadastro.items():
        print(f' - {x} tem o valor {y}')
else:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro['contratacao'] - nascimento + 35
    print('-=' * 30)
    for x, y in cadastro.items():
        print(f' - {x} tem o valor {y}')






