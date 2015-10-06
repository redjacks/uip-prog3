# Quiz 3
# Dado un intervalo de tiempo en segundos, calcular los segundos
# restantes que corresponden para convertirse exactamente en minutos.
# Este programa debe funcionar para 5 oportunidades

intentos = 5
x = 1
while x <= intentos:

	tiempo = int (input("Introduzca un intervalo de tiempo en segundos: "))
	aux = 60
	n = 1
	
	while aux <= tiempo:
		aux += 60
		n += 1
		
	t_restante = aux - tiempo
	print("Los segundos restantes para llegar al proximo minuto son: " +str(t_restante))
	x +=1
	
		
	
