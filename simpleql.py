import time
import json
import os

db = []

def dbempty():
    if db:
        return False
    else:
        return True

def cargar(listf):
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
                time.sleep(1)
                print(" -- Carga Completa -- ", nombre + extension,"\n")
            else:
                print(" -- El archivo no es de extensión .json -- ")
        else:
            print(" -- Fichero no encontrado -- ")


#cargar()

def seleccion(solicitud, busqueda): #SELECCIONAR x, y, z/* DONDE n = m
    if not dbempty():
        if busqueda:
            find = False
            for registro in db:
                #print("\n", busqueda, "\n")
                #print("valida item")
                if registro[busqueda[0]] == busqueda[1]:
                    find = True
                    if solicitud == "*":
                        reg = []
                        reg.extend(registro.items())
                        for r in reg:
                            print(r[0], ": ", r[1])  #, "   Type: ", type(r[1])
                    else:
                        for s in solicitud:
                            print(s, ": ", registro[s])  #, "   Type: ", type(registro[s])
                            #datos.append(registro[s])
                    print()
                elif busqueda[0] == "nombre" and registro[busqueda[0]].lower() == busqueda[1]:
                    find = True
                    if solicitud == "*":
                        reg = []
                        reg.extend(registro.items())
                        for r in reg:
                            print(r[0], ": ", r[1])  #, "   Type: ", type(r[1])
                    else:
                        for s in solicitud:
                            print(s, ": ", registro[s])  #, "   Type: ", type(registro[s])
                            #datos.append(registro[s])
                    print()
            if not find:
                print (" -- NINGUNA COINCIDENCIA -- ")
        elif solicitud == "*":
            for registro in db:
                reg = []
                reg.extend(registro.items())
                for r in reg:
                    print(r[0], ": ", r[1])  #, "   Type: ", type(r[1])
                print()
        else:
            for s in solicitud:
                print(s, ": ", registro[s])  #, "   Type: ", type(registro[s])

    else:
        print(" -- NO HAY REGISTROS EN MEMORIA -- ")

    
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


# PYTHON\2S 2020\201709020_PracticaLFP\ejemplo.json, PYTHON\2S 2020\201709020_PracticaLFP\ejemplo2.json