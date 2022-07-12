def contador(* num):  # os asteristico, significa desempacotar. Ou seja, ele separar todos os dados que foram dados. 
    for valor in num:
        print(f'{valor} ', end='')
    print("FIM")


contador(2, 3, 5)
contador(2,3,4,8,6)


print()


def quantidade(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e a quantidade é {tam}')

quantidade(2, 3, 5)
quantidade(2,3,4,8,6)