try:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    print(num1/num2)
except ZeroDivisionError:
    print("No se puede dividir por 0")
except ValueError:
    print("No se puede convertir el valor")