# Quiz 5 II parte

import claseHola as h

if __name__ == '__main__':
	opcion = 0
	__contador = 0
	Mensaje = h.Hola(__contador)
	while True:
		Mensaje.mostrarMenu()
		try:
			opcion = int(input("Indica una opcion: "))
		except:
			print("Opcion no valida")
		else:
			if opcion == 1:
				mensaje = input("Introduzca un mensaje para comparar: ")
			elif opcion == 2:
				Mensaje.compararMensaje(mensaje)
			elif opcion == 3:
				archivo = input("Archivo a guardar: ")
				Mensaje.guardarMensaje(archivo,mensaje,__contador)
			elif opcion == 4:
				Mensaje.mostrarContador(__contador)
			elif opcion == 5:
				break
			else:
				print("Opcion no valida")
				Mensaje.mostrarMenu()
	print("Adios!")

		