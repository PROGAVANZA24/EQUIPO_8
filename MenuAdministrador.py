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

from ProgramaPrincipal import Video
if (Tabla=='V'):
    Video1={
            'IdVideo':1,
            'Nombre': 'Diferencias entre combinaciones y permutaciones',
            'URL':'www.mate2.com',
            'Fecha Publicacion': '12/02/15'
        }
    Video2={
            'IdVideo':2,
            'Nombre': 'Diferencias entre mezclas homogeneas y heterogeneas',
            'URL':'www.quimik.com',
            'Fecha Publicacion': '15/04/21'
        }
    print('Cómo desea hacer su consulta')
    print('a=Por Id')
    print('b= Desea ver la información completa')
    respuesta=input()
    if (respuesta=='a'):
        a=Video1['IdVideo']
        print('IdVideo1: ',a)
        a=Video2['IdVideo']
        print('IdVideo2: ',a)
    else:
        print(Video1)
        print(Video2)
f=open('c:/Users/clara/OneDrive/Escritorio/Programas/Video.txt','w',encoding='utf8')
f.close
from ProgramaPrincipal import CursoTemaVideo
if (Tabla=='CTV'):
    CTV1={
            'IdCTV':1,
            'IdCT': 1,
            'Video': 'Diferencias entre combinaciones y permutaciones'
        }
    CTV2={
            'IdCTV':2,
            'IdCT': 2,
            'Video': 'Diferencias entre mezclas homogeneas y heterogeneas'
        }
    print('Cómo desea hacer su consulta')
    print('a=Por Id')
    print('b= Desea ver la información completa')
    respuesta=input()
    if (respuesta=='a'):
        a=CTV1['IdCTV']
        print('IdCTV1: ',a)
        a=CTV2['IdCTV']
        print('IdCTV2: ',a)
    else:
        print(CTV1)
        print(CTV2)
f=open('c:/Users/clara/OneDrive/Escritorio/Programas/CursoTemaVideo.txt','w',encoding='utf8')
f.close

from ProgramaPrincipal import CursoTema
if (Tabla=='CT'):
    CT1={
            'IdCT':1,
            'IdCurso':1,
            'IdVideo':1
        }
    CT2={
            'IdCT':2,
            'IdCurso':2,
            'IdVideo':2
        }
    print('Cómo desea hacer su consulta')
    print('a=Por Id')
    print('b= Desea ver la información completa')
    respuesta=input()
    if (respuesta=='a'):
        a=CT1['IdCT']
        print('IdCT1: ',a)
        a=CT2['IdCT']
        print('IdCT2: ',a)
    else:
        print(CT1)
        print(CT2)
f=open('c:/Users/clara/OneDrive/Escritorio/Programas/CursoTema.txt','w',encoding='utf8')
f.close
from ProgramaPrincipal import Curso
if (Tabla=='C'):
    Curso1={
            'IdCurso': 1,
            'Descripcion': 'Probabilidad: Combinaciones y Permutaciones',
            'IdEmpleado': 1
        }
    Curso2={
            'IdCurso': 2,
            'Descripcion': 'Quimica: Mezclas homogeneas y heterogeneas',
            'IdEmpleado': 2
        }
    print('Cómo desea hacer su consulta')
    print('a=Por Id')
    print('b= Desea ver la información completa')
    respuesta=input()
    if (respuesta=='a'):
        a=Curso1['IdCurso']
        print('IdCurso1: ',a)
        a=Curso2['IdCurso']
        print('IdCurso2: ',a)
    else:
        print(Curso1)
        print(Curso2)
f=open('c:/Users/clara/OneDrive/Escritorio/Programas/Curso.txt','w',encoding='utf8')
f.close

from ProgramaPrincipal import Empleado
if (Tabla=='E'):
    Empleado1={
            'IdEmpleado': 1,
            'Nombre': 'Kim Seok Jin ',
            'Direccion': 'Apodaca, N.L.'
        }
    Empleado2={
            'IdEmpleado': 2,
            'Nombre': 'Kim Namjoon',
            'Direccion': 'Apodaca, N.L.'
        }
    print('Cómo desea hacer su consulta')
    print('a=Por Id')
    print('b= Desea ver la información completa')
    respuesta=input()
    if (respuesta=='a'):
        a=Empleado1['IdEmpleado']
        print('IdEmpleado1: ',a)
        a=Empleado2['IdEmpleado']
        print('IdEmpleado2: ',a)
    else:
        print(Empleado1)
        print(Empleado2)
f=open('c:/Users/clara/OneDrive/Escritorio/Programas/Empleado.txt','w',encoding='utf8')
f.close