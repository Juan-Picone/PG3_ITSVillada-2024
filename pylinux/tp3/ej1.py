aux = 1
while aux == 1:
    try:
        var1 = int (input("ingrese un numero: "))
        var2 = int (input("ingrese otro numero: "))
    except ValueError:
        print("No se puede ingresar letras")
    finally:
        print(x1+x2)
        aux = input("desea continuar? 1. Si / 2.No")
        if aux == 2:
            break
        elif aux == 1
    :
            continue
    