# Quiz #2
# "El Emperador" esta celebrando aniversario y ofrecera a sus clientes las siguientes ofertas:
# >= $500, 30% descuento
# < $500 y >= $200, 20% descuento
# < $200 y >= $100, 10% descuento
# Elabore el programa para 5 usuarios por ejecucion

usuarios = 5
i = 1

while i <= usuarios:
	
	print("Cliente " +str(i))
	
	compra = float(input("   Introduzca el monto de la compra: $"))

	descuento = 0
	
	if compra >= 500:
		descuento = compra*0.3
		
	elif ((compra <500) and (compra >=200)):
		descuento = compra*0.2

	elif ((compra <200) and (compra >=100)):
		descuento = compra*0.1
		 

	print("   El descuento de la compra es por $" +str(descuento))

	i+= 1

else:

	print("Fin de Programa. Adios.")
