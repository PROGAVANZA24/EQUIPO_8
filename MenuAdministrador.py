from ProgramaPrincipal import Tema
from ProgramaPrincipal import Video
from ProgramaPrincipal import CursoTemaVideo
from ProgramaPrincipal import CursoTema
from ProgramaPrincipal import Curso
from ProgramaPrincipal import Empleado

print('Qué tabla desea consultar')
print('T= Tabla de Tema')
print('V= Tabla de Video')
print('CTV= Tabla de Curso Tema Video')
print('CT= Tabla de Curso Tema')
print('C=Tabla de Curso')
print('E= Tabla de Empleados')
Tabla=input()


from ProgramaPrincipal import Tema
if (Tabla=='T'):
    Tema1={
            "IdTema":1,
            "Nombre":"Combinaciones y Permutaciones"
        }
    Tema2={
            "IdTema":2,
            "Nombre":"Mezclas homogeneas y heterogeneas"
        }
    print('Cómo desea hacer su consulta')
    print('a=Por Id')
    print('b= Desea ver la información completa')
    respuesta=input()
    if (respuesta=='a'):
        a=Tema1['IdTema']
        print('IdTema1: ',a)
        a=Tema2['IdTema']
        print('IdTema2: ',a)
    else:
        print(Tema1)
        print(Tema2)
f=open('c:/Users/clara/OneDrive/Escritorio/Programas/Tema.txt','w',encoding='utf8')
f.close