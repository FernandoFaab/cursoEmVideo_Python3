def dobra(list):  # criei uma def que dobra valores
    pos = 0  # criei um contador
    while pos < len(list):  # enquanto o contador for menor que o tamnho da lista ele vai dobrar os valores.
        list[pos]*=2  # o valor que será dobrado.
        pos += 1  # aumenta o cantador para passar para o próximo item da lista.

valores = [1,2,3,4,5]  # valores da lista.
dobra(valores)  # acionando a func dobra, para dobrar os valores da lista acima.
print(valores)  # printando a lista, depois de fazer a dobra.


