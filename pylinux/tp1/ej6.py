vocales = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
palabra = str(input("ingrese una palabra: "))

for i in range(len(palabra)):
    if palabra[i] in vocales:
        print(f"la vocal {palabra[i]} se encuentra en la posicion {i}")