#!/usr/bin/phyton

import sys

try:
	x = float(sys.argv[2])
	y = float(sys.argv[3])
except ValueError:
	print("Error: datos incorrectos")
	exit()
		    

	
if len(sys.argv) != 4:
	print("Error: calculadora.py funcion operando1 operando2")
	exit()
			
if sys.argv[1] == "sumar":
	suma = x + y
	print str(suma),
elif sys.argv[1] == "restar":
	resta = x - y
	print str(resta),
elif sys.argv[1] == "multiplicar":
	multi = x * y
	print str(multi),
elif sys.argv[1] == "dividir":
	try:
		div = x / y
		print str(div),
	except ZeroDivisionError:
		print("Imposible dividir por 0")
		exit()
else:
	print("Error: La funcion no es correcta"),
