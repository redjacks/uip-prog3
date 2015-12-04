# Tarea - Lista de supermercados
## Instrucciones:
# Usted fue contratado por la startup ABC como programador. 
#Ellos le solicitan que programe la primera fase de un módulo que represente una lista de supermercados. 
#El programa debe presentar un menú donde pueda elegir, por lo poco, si quiero agregar, eliminar y ver los elementos de mi lista de supermercado. 
#Se pueden manejar hasta 3 listas de supermercado. ABC está interesada en funciones, manejo de excepciones y módulos. 
#Este código debe servir para posteriores proyectos.

import menuSupermerc as M
import agregarElemento as A
import eliminarElemento as E
import verElemento as V

if __name__ == '__main__':
    
	opcion_1 = 0
	opcion_2 = 0
	lista_A = []
	lista_B = []
	lista_C = []
	lista = []
	lista.append(lista_A)
	lista.append(lista_B)
	lista.append(lista_C)
    
	while opcion_1 != 4:
		
		M.menu_listas()
		
		try:
			opcion_1= int(input("Indica una opcion (1-4): "))
        
		except:
			print("Opcion no valida")
        
		else:
           
			if opcion_1 == 4:
				print ("Adios.")
				break
			
			if opcion_1 >= 5 or opcion_1 <= 0:
				print ("Opcion no valida.")
				break
				
			else: 
				
				M.menu_operaciones()
				
				try:
					
					opcion_2 = int(input("Indica una opcion (1-4): "))
				
				except:
					print("Opcion no valida")
				
				else:
					
					if opcion_2 == 4:
						break
						
					if opcion_2 >= 5 or opcion_2 <= 0:
						print ("Opcion no valida.")
						break
					
					else:
						
						if opcion_2 == 1:
							if opcion_1 == 1:
								V.verElemento(lista_A)
							if opcion_1 == 2:
								V.verElemento(lista_B)
							if opcion_1 == 3:
								V.verElemento(lista_C)
							
						if opcion_2 == 2:
							if opcion_1 == 1:
								A.agregarElemento(lista_A)
							if opcion_1 == 2:
								A.agregarElemento(lista_B)
							if opcion_1 == 3:
								A.agregarElemento(lista_C)
							
						if opcion_2 == 3:
							if opcion_1 == 1:
								E.eliminarElemento(lista_A)
							if opcion_1 == 2:
								E.eliminarElemento(lista_B)
							if opcion_1 == 3:
								E.eliminarElemento(lista_C)
							
	print("Hasta luego!")
