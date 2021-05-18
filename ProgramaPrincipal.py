class Tema:
    def _init_(self,IdTema,Nombre):
        self.IdTema=IdTema
        self.Nombre=Nombre
    def display(self):
        print(f'IdTema: {self.IdTema},Nombre: {self.Nombre}')