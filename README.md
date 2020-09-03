# 201709020_PracticaLFP

MANUAL DE USUARIO


:::::::::::::::::::::::::::SIMPLEQL:::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

INFORMACIÓN GENERAL:

SimpleQL es un lenguaje declarativo que permitirá al usuario cargar 

registros desde un archivo --.json-- y realizar consultas atraves de 

comandos.

El entorno de simpleql es por medio de consola con una presentación 

amigable de las consultas realizadas, trabaja con case insensitive.


SIMPLEQL:

Al iniciar simpleql observará el titulo de presentación.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::SimpleQL:::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

|

A continuación deberá cargar los archivos JSON para almacenar los registros 

en memoria, con el comando CARGAR.

	CARGAR archivo1.json

Si necesita cargar varios archivos utilice el formato:
	
	CARGAR archivo1.json, archivo2.json, archivo3.json

Luego se mostrará un mensaje del estado de la carga.

Con los registros cargados en memoria, puede hacer uso de los siguientes 

comandos:

    COMANDO [SELECCIONAR #]:Es una consulta que mostrará en tablas de lo 

solicitado

	SELECCIONAR -atributo-                            -> Se podrán 

seleccionar todos ("*") o los que indique con el formato "atributo1, 

atributo2, atributoN"
		Ejemplo: SELECCIONAR *
			 SELECCIONAR nombre, edad

	SELECCIONAR -atributo- DONDE -atributo- = valor   -> La consulta se 

puede condicionar con el modificador DONDE (sin condiciones multiples), el 

cual deberá ser seguido por un atributo, el signo "=" y el valor de 

búsqueda, si el atributo es nombre el valor de búsqueda deberá ser 

ingresado entre comillas:
		Ejemplo: SELECCIONAR nombre, edad DONDE edad = 25
			 SELECCIONAR nombre, edad DONDE nombre = "Antonio"
	
    COMANDO [MAXIMO #]:Obtendrá el valor máximo de un tipo de dato

	MAXIMO (edad/promedio)  -> Solo será valido para atributos de tipo 

numérico.
		Ejemplo: MAXIMO edad
			 MAXIMO promedio
	
    COMANDO [MNIMO #]:Obtendrá el valor minimo de un tipo de dato

	MNIMO (edad/promedio)  -> Solo será valido para atributos de tipo 

numérico.
		Ejemplo: MINIMO edad
			 MINIMO promedio
	
    COMANDO [SUMA #]: Sumará todos los valores segun el atributo que 

especifique
	SUMA (edad/promedio)   -> Solo será valido para atributos de tipo 

numérico.
		Ejemplo: SUMA edad
			 SUMA promedio

    COMANDO [CUENTA]: Contará el número de registros
		Ejemplo: CUENTA    

    COMANDO [REPORTAR N]: Generará un reporte en html, N indica la cantidad 

de registros a mostrar en el reporte
		Ejemplo: REPORTAR 15

    COMANDO EXTRA:
	END   -> Finalizará el programa
