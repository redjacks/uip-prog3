# Quiz 3
# Dado un intervalo de tiempo en segundos, calcular los segundos
# restantes que corresponden para convertirse exactamente en minutos.
# Este programa debe funcionar para 5 oportunidades

x = 1
while x <= 5:

	tiempo = int (input("Introduzca un intervalo de tiempo en segundos: "))
	aux = 60
	
	while aux <= tiempo:
		aux += 60
		
	t_restante = aux - tiempo
	print("Los segundos restantes para llegar al proximo minuto son: " +str(t_restante))
	x +=1
	
		
	
