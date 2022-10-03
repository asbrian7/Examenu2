#Examen unidad II
#Avalos Sanchez Brian
import sys

try:
    archivo = open("Estudiantes.prn", mode="r" ,encoding="ISO-8859-1")
except FileNotFoundError:
    print("no existe el archivo Estudiantes")
    sys.exit()
try:
    archivo2 = open("Kardex.txt", mode="r" ,encoding="ISO-8859-1")
except FileNotFoundError:
    print("no existe el archivo Kardex")
    sys.exit()

# 1. Crear un método que regrese un conjunto de tuplas de estudiantes.
ConjEstudiante = set()
estudiante = [] #conjunto
tupla=()
if archivo.readable():
    i=0
    estudiante = archivo.read().split("\n")
    for mun in estudiante[0:]:
        i +=1
        nc = estudiante[i - 1][0:8]
        nom = estudiante[i - 1][8:]
        tupla=(nc,nom)
        ConjEstudiante.add(tupla)
print(ConjEstudiante)
#2. Crear un método que regrese un conjunto de tuplas de materias.
def regresa_conjunto_promedios():
    conjMateria = set()
    materias = [] #conjunto
    if archivo2.readable():
        materia = archivo2.readlines()
        for renglones in materia:
            mat=renglones.split("|")
            #print(mat)
            tupla1 = (mat[0],mat[1],mat[2][:-1])
            conjMateria.add(tupla1)
    print(conjMateria)

#2. Crear un método que regrese un conjunto de tuplas de materias.
conjMateria = set()
materias = [] #conjunto
if archivo2.readable():
    materia = archivo2.readlines()
    for renglones in materia:
        mat=renglones.split("|")
        #print(mat)
        tupla1 = (mat[0],mat[1],mat[2][:-1])
        conjMateria.add(tupla1)
print(conjMateria)

import json
lista = [18420427, 18420424,18420428,18420447]
def metodo(nctrl):
    ni=int(len(nctrl))
    cont=0
    mJason = open("alum.json", mode="w")
    #Muestre todos los alumnos al estar vacio

    #muestra los de la cadena
    while cont < ni:
        nc = str(nctrl[cont])
        cadena = {}
        materia = []
        promedioG = 0
        for alumno in ConjEstudiante:
            if (str(alumno[0]) == nc):
                cad = {}
                for mat in conjMateria:
                    if (str(alumno[0]) == str(mat[0])):
                        materia.append({"Nombre:": mat[1]})
                cad = {"Nombre": alumno[1], "Materias": materia}
        json.dump(cad, mJason)
        cont = cont + 1
        print(cont)

    archivo.close()
    archivo2.close()

metodo(lista)

#4 lista de materias
def regresa_materias_por_estudiante(ctrl):
    promedios = regresa_conjunto_promedios()
    lista_materias = []
    for mat in promedios:
        c,m,p = mat #destructurar la variable mat
        if ctrl ==c:
            lista_materias.append({"Nombre":m})
    return json.dumps(lista_materias)


