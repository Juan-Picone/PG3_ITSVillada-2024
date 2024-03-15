def es_numero_step(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        if abs(int(numero_str[i]) - int(numero_str[i+1])) != 1:
            return False
    return True

numero = int(input("Introduce un numero: "))

print(es_numero_step(numero))