def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')

somar(2,5,1)  # esta soma vai funcionar normal.
somar(2,3)  # Esta soma não vai funcionar, porque eu não informei o terceiro parâmetro.
somar(b=4,c=2)  # não informei o A, mas ele vai receber zero, pois o parâmetro na declaração esta pré determinada. 
"""
Para caso eu não informe todos os parâmetros, eu posso deixar os parâmetros lá na def, já pré determinados, colocando
= 0 
ou seja, deixando um valor opcional. Assim se não for informado um parâmetro, a função vai funcionar normal, pois o 
parâmetro foi predefinido com 0, ou como valor opcional. 
"""