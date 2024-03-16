class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self. lado3 = lado3

    def LadoMayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es: ", self.lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado mayor es: ", self.lado2)
        else:
            print("El lado mayor es: ", self.lado3)
        
    def esEquilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es equilatero")
        else:
            print("No es equilatero")

triangulo1 = Triangulo(5, 5, 5)
triangulo1.LadoMayor()
triangulo1.esEquilatero()


