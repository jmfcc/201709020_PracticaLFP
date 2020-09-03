import simpleql
from time import sleep

#sistema = ["cargar", "seleccionar", "donde", "minimo", 
#          #"maximo", "suma", "cuenta", "reportar"]
#simb = ["*", ",", "=", "\""]

atr = ["nombre", "edad", "activo", "promedio"]
print("\n\n\t:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("\t::::::::::::::::::::::::::: SIMPLEQL ::::::::::::::::::::::::::::::")
print("\t:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n")

def concatena(tokens):
    cadena = ""
    init = True
    for tok in tokens:
        if init:
            cadena = tok
            init = False
        else:
            cadena = cadena + " " + tok
    return cadena

def removeSpaces(listaElementos):
    listaElementos = listaElementos.split(" ")
    while listaElementos.__contains__(""):
        listaElementos.remove("")
    return listaElementos

while True:
    comando = input()
    
    if comando:
        #comando = comando.lower()
        tokens = removeSpaces(comando)
        #print(tokens)
        if tokens and (len(tokens) > 1 or tokens[0].lower() == "cuenta"):
            tokens[0] = tokens[0].lower()
            #print("tiene tokens ------")
            if tokens[0] == "cargar":
                tokens.remove("cargar")
                listfiles = concatena(tokens) # <---
                if listfiles:
                    listf = listfiles.strip().split(", ")
                    simpleql.cargar(listf)
            elif tokens[0].lower() == "seleccionar":
                tokens.remove("seleccionar")
                select = concatena(tokens).lower()
                copyatr = atr.copy()
                #print(type(copyatr), " ", copyatr)
                if select.__contains__(" donde ") and select.__contains__(" = "):
                    tokens = select.split(" donde ") # lista solicitud / busqueda
                    #busqueda  (attr = )
                    #print(tokens[1])
                    tokens[1] = concatena(removeSpaces(tokens[1]))
                    tokens[0] = concatena(removeSpaces(tokens[0]))
                    #print(tokens[1])
                    busqueda = tokens[1].split(" = ") # atributo / valor
                    contcomm = tokens[0].count(",")
                    contesp = tokens[0].count(" ")
                    solicitud = tokens[0].split(", ")
                    #print(busqueda)
                    if contcomm == (len(solicitud) - 1) and contcomm == contesp:
                        #print(solicitud)
                        valida = True
                        for s in solicitud:
                            if copyatr.__contains__(s):
                                #print("compara")
                                copyatr.remove(s)
                            elif s == "*" and len(solicitud) == 1:
                                #print("si reconoce ", s, "  de ", solicitud)
                                solicitud = "*"
                                break
                            else:
                                print(" -- Error lexico en atributos solicitados --")
                                valida = False
                                break
                        if valida:
                            #print("Se mantiene valido")
                            if len(busqueda) == 2:
                                if atr.__contains__(busqueda[0]):
                                    if busqueda[0] == "nombre" and busqueda[1].count("\"") == 2:
                                        if busqueda[1][0] == "\"" and busqueda[1][len(busqueda[1]) - 1] == "\"":
                                            busqueda[1] = concatena(removeSpaces(concatena(busqueda[1].split("\""))))
                                            #print(busqueda)
                                            simpleql.seleccion(solicitud, busqueda)
                                        else:
                                            print(" -- Error sintactico de valor de busqueda --")
                                    elif not (busqueda[0] == "nombre") and not (busqueda[1].count("\"") == 2):
                                        try:
                                            #print(busqueda)
                                            if busqueda[0] == "edad":
                                                busqueda[1] = int(busqueda[1])
                                                simpleql.seleccion(solicitud, busqueda)
                                            elif busqueda[0] == "promedio":
                                                busqueda[1] = float(busqueda[1])
                                                simpleql.seleccion(solicitud, busqueda)
                                                #print("parseando")
                                            elif busqueda[0] == "activo":
                                                if busqueda[1] == "true" or busqueda[1] == "false":
                                                    busqueda[1] = (busqueda[1] == "true")
                                                    simpleql.seleccion(solicitud, busqueda)
                                                else:
                                                    print(" -- Error de valor de búsqueda -- ")
                                                    break
                                            #print("solicitud terminada")
                                        except:
                                            print(" -- Error de valor de búsqueda -- ")
                                    else:
                                        print(" -- Error de sintaxis de busqueda--")
                                else:
                                    print(" -- Error de atributo de búsqueda --")
                            #print (tokens)
                    else:
                        #print(solicitud, "   ", contcomm)
                        print(" -- Error sintactico de atributos solicitados --")
                elif not select.__contains__("donde"):
                    tokens = concatena(tokens)
                    contcomm = tokens.count(",")
                    contesp = tokens.count(" ")
                    solicitud = tokens.split(", ")
                    #print(busqueda)
                    #print(tokens, "  ", contcomm, "  ", contesp, "  ", solicitud)
                    if contcomm == (len(solicitud) - 1) and contcomm == contesp:
                        #print(solicitud)
                        valida = True
                        for s in solicitud:
                            if copyatr.__contains__(s):
                                #print("compara")
                                copyatr.remove(s)
                            elif s == "*" and len(solicitud) == 1:
                                #print("si reconoce ", s, "  de ", solicitud)
                                solicitud = "*"
                                break
                            else:
                                print(" -- Error lexico en atributos solicitados --")
                                valida = False
                                break
                        if valida:
                            simpleql.seleccion(solicitud, None)
                    else:
                        print(" -- Error sintactico de atributos solicitados --")
                else:
                    print(" -- Error de sintaxis -- ")
            elif tokens[0].lower() == "minimo":
                tokens.remove("minimo")
                atrmin = concatena(tokens).lower()
                if atrmin == "edad" or atrmin == "promedio":
                    simpleql.getminimo(atrmin)
                else:
                    print(" -- Atributo no válido -- ")
            elif tokens[0].lower() == "maximo":
                tokens.remove("maximo")
                atrmax = concatena(tokens).lower()
                if atrmax == "edad" or atrmax == "promedio":
                    simpleql.getmaximo(atrmax)
                else:
                    print(" -- Atributo no válido -- ")
            elif tokens[0].lower() == "suma":
                tokens.remove("suma")
                atrsum = concatena(tokens).lower()
                if atrsum == "edad" or atrsum == "promedio":
                    simpleql.suma(atrsum)
                else:
                    print(" -- Atributo no válido -- ")
            elif tokens[0].lower() == "cuenta":
                if len(tokens) == 1:
                    simpleql.cont()
                else:
                    print(" -- Error de comando -- ")
            elif tokens[0].lower() == "reportar":
                if len(tokens) == 2:
                    try:
                        n = int(tokens[1])
                        if n <= 0:
                            print(" --- Error de cantidad solicitada --- ")
                        elif n <= simpleql.dblength():
                            simpleql.reportar(n)
                        else:
                            print(" -- La cantidad de registros solicitados exede a los existentes -- ")
                    except:
                        print(" -- Error de numero de registros a reportar -- ")
                else:
                    print(" -- Error de comando -- ")
            else:
                print(" -- Comando no válido -- ")
        else:
            if tokens[0].lower() == "end":
                break
            else:
                print(" -- Error de sintaxis -- \n")
        #print(tokens)
        #print()
    #tx = "\"Juan\""
    #t = tx.split("\"")
    print()
    #comando = ""


# Seleccionar nombre, promedio donde nombre = "Juan"
# seleccionar nombre, promedio donde promedio = 43