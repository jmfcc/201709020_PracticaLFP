import time
import json
import os

db = []

def cargar():
    listfiles = input("Ingrese los archivos a cargar: ")
    if listfiles:
        listf = listfiles.strip().split(",")
    else:
        print("\nDebe ingresar las direcciones de los archivos")
        time.sleep(1)
        return
    for f in listf:
        if os.path.isfile(f):
            ph, fh = os.path.split(f)
            nombre, extension = os.path.splitext(fh)
            if extension.__eq__(".json"):
                files = open(f)
                datosjson = json.load(files) #Se carga los datos como diccionarios
                #db.append(datosjson)
                db.extend(datosjson)
                #print(datosjson)
            else:
                print("El archivo no es de extensión .json")
        else:
            print("El fichero no existe")

    print(" -- Carga Completa -- \n")
    time.sleep(2)

cargar()

def seleccion(solicitud, busqueda): #SELECCIONAR x, y, z/* DONDE n = m
    if busqueda:
        for registro in db:
            #print("\n", registro, "\n")
            if registro[busqueda[0]] == busqueda[1]:
                #datos = []
                if solicitud == "*":
                    reg = []
                    reg.extend(registro.items())
                    for r in reg:
                        print(r[0], ": ", r[1])  #, "   Type: ", type(r[1])
                else:
                    for s in solicitud:
                        print(s, ": ", registro[s])  #, "   Type: ", type(registro[s])
                        #datos.append(registro[s])
                return
    elif solicitud == "*":
        for registro in db:
            reg = []
            reg.extend(registro.items())
            for r in reg:
                print(r[0], ": ", r[1])  #, "   Type: ", type(r[1])
            print()

    
#req = ["nombre", "edad", "promedio"]
#reqall = "*"
#busq = ["nombre", "registro 3"]
#busq2 = ["promedio", 60.5]
#b = ""
#seleccion(reqall, b)

def max(tipo): #MAXIMO edad/promedio
    maximo = 0
    init = True
    for registro in db:
        if init:
            maximo = registro[tipo]
            init = False
        else:
            if maximo < registro[tipo]:
                maximo = registro[tipo]
    print(tipo, ": ", maximo)

#max("promedio")

def min(tipo): #MINIMO edad/promedio
    minimo = 0
    init = True
    for registro in db:
        if init:
            minimo = registro[tipo]
            init = False
        else:
            if minimo > registro[tipo]:
                minimo = registro[tipo]
    print(tipo, ": ", minimo)

#min("edad")

def suma(tipo): #SUMA edad/promedio
    sumatoria = 0
    init = True
    for registro in db:
        if init:
            sumatoria = registro[tipo]
            init = False
        else:
            sumatoria = sumatoria + registro[tipo]
    print(tipo, ": ", sumatoria)

#suma("promedio")

def cont(): #CUENTA
    print("# Registros: ", len(db))

#cont()

def reportar(n):
    pass


# PYTHON\2S 2020\201709020_TareasLFP\Practica\ejemplo.json,PYTHON\2S 2020\201709020_TareasLFP\Practica\ejemplo.json