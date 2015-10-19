# Quiz 4
# Desarrolle una aplicacion que guarde, en un archivo de texto,
# la calificacion de 5 quizzes realizados por 3 estudiantes.
# Cada estudiante tendra su propio archivo de texto, cuyo nombre
# de archivo sera igual al nombre del estudiante. Ademas debe mostrar
# en pantalla el valor promedio de las calificaciones del estudiante.
# Utilice todos los conceptos aprendidos hasta el momento.

def agregarNotas(notas, nombre, nota):
	notas[nombre] = nota

def guardarNotas(notas, archivo):
	out_file = open(archivo, "wt")
	for k, v in notas.items():
		out_file.write(k + "," + v + "\n")
	out_file.close()

def cargarNotas(notas, archivo):
	in_file = open(archivo, "rt")
	while True:
		in_line = in_file.readline()
		if not in_line:
			break
		in_line = in_line[:-1]
		nombre, nota = in_line.split(",")
		notas[nombre] = nota
	in_file.close()

def calcularPromedio(notas):
	total = 0
	for x in notas.items():
		total += notas 
	promedio = total/5
	print("Promedio de quiz: " +str(promedio))

def mostrarMenu():
	print('1. Imprimir promedio')
	print('2. Agregar notas')
	print('3. Guardar notas')
	print('4. Cargar notas')
	print('5. Salir')
	print()

if __name__ == '__main__':
	notas_quiz = {}
	opcion_menu = 0
	while True:
		mostrarMenu()
		try:
			opcion_menu = int(input("Indica una opcion (1-5): "))
		except:
			print("Opcion no valida")
		else:
			if opcion_menu == 1:
				calcularPromedio(notas_quiz)
			elif opcion_menu == 2:
				print("Agregar nombre y notas(5)")
				nombre = input("nombre: ")
				notes = input("notas: ")
				agregarNotas(notas_quiz, nombre, notes)
			elif opcion_menu == 3:
				archivo = nombre
				guardarNotas(notas_quiz, archivo)
			elif opcion_menu == 4:
				archivo = input("Archivo a cargar: ")
				cargarNotas(notas_quiz, archivo)
			elif opcion_menu == 5:
				break
			else:
				print("Opcion no valida")
				mostrarMenu()
	
	print("Hasta luego.")
