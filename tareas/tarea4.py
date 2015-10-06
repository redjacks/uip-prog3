# TAREA 4
# 1. Dado un intervalo de tiempo en minutos, calcular los días, horas y minutos correspondientes.

tiempo = int (input("Introduzca un intervalo de tiempo en minutos: "))

dias = int (tiempo/1440)
tiempo = tiempo - dias*1440
horas = int (tiempo/60)
tiempo = tiempo - horas*60
minutos = tiempo

print("El tiempo es: " +str(dias) +" dias, " +str(horas) +" horas, y " +str(minutos) +" minutos.")



# 2. ¿Qué es __main__ y cómo funciona?
#
# Es un truco que existe en Python para que nuestros archivos puedan actuar como modulos reutilizables
# o como programas independientes. Como ejemplo tenemos el siguiente programa:
# $ cat mymath.py
# def square(x):
# 	return x * x
# if __name__ == '__main__':
# 	print "test: square(42) ==", square(42)
# 
# $ cat mygame.py
# import mymath
# print "this is mygame."
# print mymath.square(17)
#
# Para correr el programa de forma independiente hacemos lo siguiente:
# $ python mymath.py
# test: square(42) == 1764
#
# Pero tambien podemos usar mymath.py como un modulo:
# $ python mygame.py
# this is mygame.
# 289
#
# No vemos la linea de 'test' que tenia mymath.py porque en este contexto mymath 
# no es el programa principal.
# 


 
	