from TratandoErros.Atividade_3_criarMenuSistema.arquivo import *
from TratandoErros.Atividade_3_criarMenuSistema.interface import *  # este * importa tudo da atividade 3 e interface.


from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Cadastrados', 'cadastrar', 'exit system'])
    if resposta == 1:
        #  opção de listar o conteúdo do arquivo.
        lerArquivo(arquivo)

    elif resposta ==2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)

    elif resposta == 3:
        cabecalho('Saindo dos sistema... Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)


