def leer_numero(numero:int):
    if numero % 2 == 0:
        for i in range(numero, -1, -2):#Como range es abierto por la derecha tengo que poner -1 en el límite inferior para incluir el 0
            print(i)
    else:
        for i in range(numero, 0, -2):
            print(i)

leer_numero(21)