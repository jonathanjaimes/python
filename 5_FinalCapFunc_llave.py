cantidadLitros = float(input("Ingrese la cantidad de litros: "))

def procesoLlave(cantidadLitros):
	if cantidadLitros < 250:
		llave = "abierta"
	elif cantidadLitros >= 250 and cantidadLitros <= 450:
		llave = "cerrada"
	else:
		llave = "cerrada"

	return llave

llave = procesoLlave(cantidadLitros)

print(f"La llave debe ser {llave}")