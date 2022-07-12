def mostraLinha():  # Este fica sendo o chamado da função.
    print('-=' * 15)  # está será a função cadastrada, pelo DEF acima.


# obs. Deve-se dar dois espaços entre uma def e o resto do código. Se não a linha depois do def fica sublinhada.
mostraLinha()  # aqui eu chamei, o que está declarado abaixo da função.
print('Olá mundo')
mostraLinha()


def mensagem(msg):  # msg é uma mensagem pré determinada, ou uma operação, que tu deixa predeterminada.
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('Olá mundo! Eu sou o Fernando')
mensagem('Olá mundo! Eu sou a tayla')


def conta(x, y):  # aqui deixei claro que serão dois valores.
    print('-' * 30)
    print(x + y)  # aqui estabeleci que os dois valores serão somados.
    print('-' * 30)


conta(10, 25)  # aqui eu declarei os dois valores, para a opreção da func DEF conta. 
