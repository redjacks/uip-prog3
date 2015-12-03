# TAREA

#*Fecha de Revisión*: 26/10/2015

## Instrucciones:
#1. Elaborar un programa en Python que encueste a 10 personas y las clasifique según el deporte que practica. 
#La lista de deportes válidos son: Ajedrez, Atletismo, Baloncesto, Fútbol, Karate, Natación, Volleyball, Flag y Ping Pong. 
#Puede darse el caso que no le guste ninguno de los deportes anteriores. 
#Si es así, entonces se puede seleccionar la opción Otros. 
#Al final el programa debe mostrar estadísticas de la encuesta e indicar cuál es el deporte con mayor preferencia de los encuestados.

print('\n')
dict_deporte = {1 : 'Ajedrez', 2: 'Atletismo', 3: 'Baloncesto', 4:'Futbol', 5: 'Karate', 6:'Natacion',
	            7:'Volleyball', 8:'Flag', 9: 'PingPong' , 10: 'Otros'}	

encuesta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range (1,11):
	for x in dict_deporte:
		print(str(x) +". " +dict_deporte[x])

	try:	
		opcion = int(input("\nIntroducir el numero correspondiente al deporte que practica: "))

	except:
		print("Opcion no valida")
			
	else:
		encuesta[opcion-1] += 1

mayor = encuesta[0]		
print("Resultados de la encuesta: ")		
for x in range (1,11):
	print (dict_deporte[x] +": " + str(encuesta[x-1]) )
	if encuesta[x-1]> mayor:
		mayor = encuesta[x-1]
		llave = dict_deporte[x]

print("\nEl deporte mas popular entre los encuestados fue: \n" +llave + ': ' + str(mayor))