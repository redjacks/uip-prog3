
def eliminarElemento(lista):
	prod = str(input ("Agregar nombre de producto: "))
	
	if prod in lista:
		indice = lista.index(prod) 
		del lista[indice]
	
	else:
		print ("Producto no encontrado.")

