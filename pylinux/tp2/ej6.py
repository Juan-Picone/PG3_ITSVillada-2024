class Familia:

    def __init__(self, papa, mama, hijos):
        self.papa = papa
        self.mama = mama
        self.hijos = hijos

    def __str__(self):
        print(f'{self.papa} {self.mama}')
        for i in self.hijos:
            print(i)
        

familia1=Familia("Pedro","Maria",["Juan","Ana"])
familia1.__str__()