forma = str(input("ingrese la forma (cuadrado, triangulo): "))

if forma == "cuadrado":
    l= int(input("ingrese la longitud del lado del cuadrado: "))
    h = int(input("ingrese la altura del cuadrado: "))
    car = str(input("ingrese el caracter a usar: "))

    for i in range(h):
        for j in range(l):
            print(car, end="")
        print()

elif forma == "triangulo":
    l= int(input("ingrese la longitud del lado del triangulo: "))
    h = int(input("ingrese la altura del triangulo: "))
    car = str(input("ingrese el caracter a usar: "))

    for i in range(h):
        for j in range(i+1):
            print(car, end="")
        print()