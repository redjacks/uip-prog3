# Quiz 3
# Dado un intervalo de tiempo en segundos, calcular los segundos
# restantes que corresponden para convertirse exactamente en minutos.
# Este programa debe funcionar para 5 oportunidades

class SegRestantes(object):

	def __init__ (self):
		pass
	def contador (self, contador):
		contador += 1
		return contador
	
	def calcSeg (self, tiempo):	
		aux = 60
		while aux <= tiempo:
			aux += 60
		t_restante = aux - tiempo
		return t_restante
		
		
		
		
