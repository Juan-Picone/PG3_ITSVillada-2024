lista = [1, 2, 3, 4, 5]
num = int(input("Ingrese el valor a buscar: "))

if num in lista:
    posicion = lista.index(num)
    print(f"El valor {num} se encuentra en la posición {posicion} de la lista.")
else:
    print(f"El valor {num} no se encuentra en la lista.")