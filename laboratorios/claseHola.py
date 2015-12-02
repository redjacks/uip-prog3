# Quiz 5
#
# Hacer una clase Hola que tenga atributos: mensaje(publico) y contador(privado)
# y metodos mostrar contador, comparar mensaje y guardar mensaje. 
# Comparar mensaje compara un mensaje introducido con Hola Mundo y determina si son iguales
# sin importar el tamano de letra. Guardar mensaje guarda el mensaje introducido y el contador en un .txt
# 
# En otro programa aparte se importa la clase Hola y genera un menu con 
# 1. Ingresar mensaje 2. Comparar 3. Guardar 4. Mostrar contador 5. Salir

class Hola(object):

	def __init__ (self, __contador):
		__contador += 1

	def mostrarContador(self, __contador):
		print(__contador)
	
	def compararMensaje(self, mensaje):
		saludo = 'Hola Mundo'
		if mensaje.lower() == saludo.lower():
			print("Los mensajes son iguales.")
		else:
			print("Los mensajes son distintos.")

	def guardarMensaje(self,archivo,mensaje,__contador):
		out_file = open(archivo,"wt")
		out_file.write(mensaje + "," + str(__contador))
		out_file.close()

	def mostrarMenu(self):
		print('1. Ingresar mensaje')
		print('2. Comparar mensaje')
		print('3. Guardar mensaje')
		print('4. Mostrar contador')
		print('5. Salir')
		print()


