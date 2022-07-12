"""
retorno de resultados
é quando eu quero que o DEF me retorne resultados, para que eu trabalhe eles como quiser.

"""

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s
# assim não irá me dar um resultado para cada conta, printando na tela. Ele vai dar a váriável o valor da conta.

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)

print(f'Meus cálculos deram {r1}, {r2} e {r3}.')