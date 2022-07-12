def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e `{f3}')
"""
fatorial de um número é calculado pela multiplicação desse número por todos os seus antecessores até chegar ao número 1.
"""

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))
# ou
if par(num):
    print('É par!')
else:
    print('Não é par!')

