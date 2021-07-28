def tomaDatos():
	valorCompra = float(input("Ingrese el valor de la compra: "))
	return valorCompra

valorCompra = tomaDatos()

#Esta función nos retorna un valor que dependerá de si el valor ingresado es mayor o menor a una cantidad específica.

def Descuento(valorCompra):

	if valorCompra > 150000:
		valorDescuento = valorCompra*0.05
		nuevoValor = valorCompra - valorDescuento
	else:
		nuevoValor = valorCompra

	
	return nuevoValor

nuevoValor = Descuento(valorCompra)

print(f"El valor de la compra es de {nuevoValor}")