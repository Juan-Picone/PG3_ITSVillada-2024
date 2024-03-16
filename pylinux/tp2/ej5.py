class Persona:
    def __init__(self):
        self.nombre = str(input("Ingresa un nombre: "))
        self.edad = int(input("Ingresa una edad: "))
        print(self.nombre, self.edad)

class Empleado(Persona):
    def __init__(self):
        self.sueldo = int(input("Ingresa un sueldo: "))

    def mostrar_sueldo(self):
        print("Su sueldo es: ", self.sueldo)
    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Paga impuestos")
        else:
            print("No paga impuestos")

persona1 = Persona()
empleado1 = Empleado()
empleado1.mostrar_sueldo()
empleado1.paga_impuestos()