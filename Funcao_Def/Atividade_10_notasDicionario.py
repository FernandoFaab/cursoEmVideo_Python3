"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""

def notas(* n, situacao=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas de alunos.
    :param situacao: opcional. Deve indicar se quer ou não, ver como está a classificação de notas do aluno.
    :return: dicionário com várias informações sobre a situação do aluno.
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if situacao:
        if r['media'] > 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'

    return r

resposta = notas(6, 8, 2, 4, situacao=True)
help(notas)
