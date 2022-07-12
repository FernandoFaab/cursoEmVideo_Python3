"""
É quando você divide o programa. Colocando o seu programa principal em um arquivo, e criando um outro arquivo .py
para colocar a parte secundaria, dos DEF, ou das formulas em neste segundo arquivo.
Ai você une os dois arquivos usando um import (e o nome do arquivo secundario)
Mas ai, antes de cada função do arquivo pricnipal, que use o calculo do secundario, você precisar colocar:
(o nome do arquivo secundario).(o nome da função)
"""
# EXEMPLO

# toda esta parte dos def eu irei copiar em outro arquivo, chamado aula_2_modularização.
"""def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    return n * 2"""

import Aula_2_Modularizacao  # aqui eu importo os códigos do arquivo Aula_2_Modularizacao

num = int(input("digite um valor: "))
fat = Aula_2_Modularizacao.fatorial(num)  # aqui eu chamo uma das funções do arquivo Aula_2_Modularizacao
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {Aula_2_Modularizacao.dobro(num)}')  # aqui eu chamo uma função de Aula_2_Modularizacao
