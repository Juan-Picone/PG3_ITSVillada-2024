class Alumno:
    def inicializar(self, nombre, calif):
        self.nombre = nombre
        self.calif = calif

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        if self.calif >= 7:
            print(f"Calificacioon: {self.calif} esta regular")
        else:
            print(f"Calificacioon: {self.calif} esta mal")

alumno1 = Alumno()
alumno1.inicializar("Geronimo Benaviedes", 8)
alumno1.imprimir()