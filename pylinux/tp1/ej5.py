def esCapicua(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

n = str(input("ingrese una palabra: "))
print(esCapicua(n))