"""
 Faça um programa que tenha uma função chamada área(),
 que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


print('CONTROLE DE TERRENOS')
print('-' * 15)


def terreno(h, b):
    area = h * b
    print(f'A área do terreno é {largura} x {comprimento}, que corresponde a: {area} m²')


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
terreno(comprimento, largura)
