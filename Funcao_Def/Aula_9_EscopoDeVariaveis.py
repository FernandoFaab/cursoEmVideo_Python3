"""
Existe escopo logal e escopo global.
Escopo local é a variavel declarada dentro da função def, e ela só funciona lá dentro.
Escopo global, é a variável declarada fora da def, então ela funciona em todo o programa.

uma variável global, pode ser alterada dentro de uma local. Mas ela não será afetada na global.
uma variavel local não pode afetar uma global.
"""

def teste(b):
    a = 8  # Eu mudei o valor da váriavel A. Mas este valor alterado, só funciona aqui dentro, e não fora, no global.
    b += 4  # b recebe b + 4 (ou seja, o valor de A + 4)
    c = 2  # C só existe aqui dentro, ou seja local. Se eu printar C lá fora, vai dar erro. Pois ele só existe local.

    print(a)  # vai printar o valor de A no escopo local.
    print(b)
    print(c)

a = 5  # variável global, pois funciona em qualquer parte do programa
teste(a)  # eu estou dando para a função teste, o valor de A que é 5

print(a)  # vai printar o valor de A no escopo global.
#  print(b)  # iria dar erro, pois B não existe fora de DEF.

def teste2(y):
    global x  # porém, se eu usar este comando dentro de uma variável, o X dentro do local afetara o X global.
    x = 2

x = 1
teste2(x)
print(f'o valor de x é {x}')  # aqui ira printar o X, como o valor que global, alterado pela função local DEF.