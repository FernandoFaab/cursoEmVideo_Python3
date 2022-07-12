"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
"""
#  Jeito que eu fiz, funciona, mas era para ter usado def
print('\033[0;0;42m~' * 30)
print('SISTEMA DE AJUDA PyHELP')
print('~' * 30)
print('\033[m')

while True:
    from time import sleep
    funcao = str(input('Escreva a função ou biblioteca: '))

    if funcao != 'fim':
        print('\033[0;0;44m~' * 30)
        print(f'Acessando o manual do comando "{funcao}"')
        print('~' * 30)
        print('\033[m')
        sleep(2)

        print('\033[7m')
        help(funcao)
        print('\033[m')
        continue

    else:
        print('\033[0;30;41m~' * 30)
        print('ATÉ LOGO!')
        print('~' * 30)
        print('\033[m')
        break
"""
from time import sleep
c = (
    '\033[m',  # sem cor
    '\033[0;30;41m',  # vermelho
    '\033[0;30;42m',  # verde
    '\033[0;30;44m',  # azul
    '\033[7m',  # invertido
)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO', 1)
