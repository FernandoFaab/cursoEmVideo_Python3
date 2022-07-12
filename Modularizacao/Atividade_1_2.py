def metade(n, format=False):
    m = n / 2
    return m if not format else moeda(m)


def dobro(n, format=False):
    d = n * 2
    return d if not format else moeda(d)


def porcentagem(n, taxa, format=False):
    p = n + (n * taxa / 100)
    return p if not format else moeda(p)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')