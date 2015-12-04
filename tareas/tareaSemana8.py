# TAREA
## Instrucciones:
#Crear una aplicación en Kivy que maneje un registro de asistencia. 
#Básicamente la aplicación debe contener una etiqueta que diga 
#"Nombre: ", un campo para ingresar cadenas de texto, un botón que diga "Guardar" y otro botón que diga "Exportar". 
#El botón para guardar agrega el contenido del campo a una lista de asistencia.
#El botón para exportar salva la lista de asistencia a un fichero con extensión TXT.

from kivy.app import App

lista = []

def guardar(name):
	lista.append(name)
	print(lista)	
	
def exportar():
	archivo = open('registro.txt', 'wt')
	archivo.write(str(lista))
	archivo.close()

class AsistenciaApp(App):
	
	def build (self):
		pass
	
	
	
if __name__ == '__main__':
	AsistenciaApp().run()

	
	
