def metade(n, format=False):
    m = n / 2
    return m if not format else moeda(m)


def dobro(n, format=False):
    d = n * 2
    return d if not format else moeda(d)


def porcentagem(n, taxa, format=False):
    p = n + (n * taxa / 100)
    return p if not format else moeda(p)


def diminuir(p, taxa=0, formato=False):
    res = p - (p * taxa /100)
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(p=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'preço analisado: \t{moeda(p)}')
    print('-' * 30)
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'A metade do preço: \t{metade(p, True)}')
    print(f'com {taxaa}% de aumento: \t{porcentagem(p, taxaa)}')
    print(f'com {taxar}% de aumento: \t\t{diminuir(p, taxar)}')
    print('-' * 30)

