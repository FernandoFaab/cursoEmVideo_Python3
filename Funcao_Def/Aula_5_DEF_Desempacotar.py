# Com esta função, eu faço somas, independente da quantidade de valores, cadastrados.

def soma(* valores):
    s = 0
    for x in valores:
        s += x
    print(f'Somando os valores {valores} temos {s}')

soma(5,3)
soma(5,3,2,1)