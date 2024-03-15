l= int(input("ingrese la longitud del lado del cuadrado: "))
h = int(input("ingrese la altura del cuadrado: "))
car = str(input("ingrese el caracter a usar: "))

for i in range(h):
    for j in range(l):
        print(car, end="")
    print()