try:
    with open('ej5.txt') as archivo:
        archivo.write(123)
except ValueError:
    print("No se puede escribir en el archivo")