anio = int(input("ingrese un año y yo le dire si es bisiesto o no: "))
if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("es bisiesto")
else:
    print("no es bisiesto")
