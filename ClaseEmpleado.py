class Empleado:
    def _init_(self,IdEmpleado,Nombre,Direccion):
        self.IdEmpleado=IdEmpleado
        self.Nombre=Nombre
        self.Direccion=Direccion
    def display(self):
        print(f'IdEmpleado: {self.IdEmpleado},Nombre:{self.Nombre},Direccion: {self.Direccion}')