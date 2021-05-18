class Tema:
    def _init_(self,IdTema,Nombre):
        self.IdTema=IdTema
        self.Nombre=Nombre
    def display(self):
        print(f'IdTema: {self.IdTema},Nombre: {self.Nombre}')

class Video:
    def _init_(self,IdVideo,Nombre,URL,FechaPublicacion):
        self.IdVideo=IdVideo
        self.Nombre=Nombre
        self.URL=URL
        self.FechaPublicacion=FechaPublicacion
    def display(self):
        print(f'IdVideo:{self.IdVideo}, Nombre: {self.Nombre}, URL: {self.URL}, Fecha Publicacion: {self.FechaPublicacion}')

class CursoTemaVideo:
    def _init_(self,IdCTV,IdCT,Video):
        self.IdCTV=IdCTV
        self.IdCT=IdCT
        self.Video=Video

class CursoTema:
    def _init_(self,IdCT,IdCurso,IdTema):
        self.IdCT=IdCT
        self.IdCurso=IdCurso
        self.IdTema=IdTema
    def display(self):
        print(f'IdCT: {self.IdCT},IdCurso: {self.IdCurso},IdTema: {self.IdTema}')

class Curso:
    def _init_(self,IdCurso,Descripcion,IdEmpleado):
        self.IdCurso=IdCurso
        self.Descripcion=Descripcion
        self.IdEmpleado=IdEmpleado
    def display(self):
        print(f'IdCurso: {self.IdCurso},Descripcion: {self.Descripcion}, IdEmpleado:{self.IdEmpleado}')