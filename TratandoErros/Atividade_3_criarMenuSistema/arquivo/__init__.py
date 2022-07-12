from TratandoErros.Atividade_3_criarMenuSistema.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # escreve um aquivo de texto e se ele não existir ele cria.
        a.close()
    except:
        print(f'\033[31mHouve um Erro, na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {nome}, criado com sucesso.\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        contador = 0
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            contador += 1
            print(f'{contador:<3}', end='')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO, na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
