class Persona:
    def inicializar(self,nombre):
        self.nombre = nombre

    def imprimir(self):
        print(f"Nombre: {self.nombre}")

persona1 = Persona()
persona1.inicializar("Geronimo Benaviedes")
persona1.imprimir()
