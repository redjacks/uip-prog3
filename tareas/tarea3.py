# Tarea 3
# Escriba un programa que imprima el factorial de un numero n con su indice

numero = int(input("Introduzca un numero entero: "))
x = 1
suma = 0

if numero > 0:
	while x <= numero:
		suma += x
		print(str(x) +" - " +str(suma))
		x += 1
else:
	print("Numero no valido")
input()
		
	


