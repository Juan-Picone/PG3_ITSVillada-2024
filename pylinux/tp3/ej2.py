try:
    num1 = int(input("ingrese un numero: "))
    num2 = int(input("ingrese otro numero: "))
    print(num1/num2)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
    