"""
Estes três códigos repetitivos, podem ser simplicados com uma função, como veremos abaixo.

a = 4
b = 5
s = a+b
print(s)

a = 8
b = 9
s = a+b
print(s)

a = 2
b = 1
s = a+b
print(s)
"""
def soma(a, b):
    s = a + b
    print(s)


soma(4,5)  # o primeiro valor sempre é A e o segundo valor sempre é B.
soma(8,9)
soma(2,1)
soma(b=5, a=3)  # Você pode inverter a ordem da declaração, especificando. Mas tem que especificar os dois.
