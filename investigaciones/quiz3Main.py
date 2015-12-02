		
import SegRestantes as seg

if __name__ == '__main__':
	count = 0
	Segundos = seg.SegRestantes()
	while count < 5 :
	
		try:
			tiempo = int (input("Introduzca un intervalo de tiempo en segundos: "))
		
		except Exception:
			print ("Entrada no valida.")
	
		else:	
			t_restante = Segundos.calcSeg(tiempo)
			print("Los segundos restantes para llegar al proximo minuto son: " +str(t_restante))
			count = Segundos.contador(count)
	
		