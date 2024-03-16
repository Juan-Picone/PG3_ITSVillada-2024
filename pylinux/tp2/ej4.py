class Operacion():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        print(self.num1 + self.num2)

    def resta(self):
        print(self.num1 + self.num2)

    def multiplicacion(self):
        print(self.num1 + self.num2)

    def division(self):
        print(self.num1 + self.num2)

operacion1 = Operacion(5, 5)
print(operacion1.suma())
print(operacion1.resta())
print(operacion1.multiplicacion())
print(operacion1.division())