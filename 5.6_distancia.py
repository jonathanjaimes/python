def valores():
	punto1 = input("Ingrese el primer punto: ")
	x1 = float(input(f"Ingrese la coordenada en x del punto {punto1}: "))
	y1 = float(input(f"Ingrese la coordenada en y del punto {punto1}: "))
	punto2 = input("Ingrese el primer punto: ")
	x2 = float(input(f"Ingrese la coordenada en x del punto {punto2}: "))
	y2 = float(input(f"Ingrese la coordenada en y del punto {punto2}: "))
	return punto1, punto2, x1, y1, x2, y2

def procedimiento(x1, y1, x2, y2):
	distancia = ( ((x1-x2)**2) + ((y1-y2)**2) ) ** (1/2)
	return distancia

def salida(punto1, punto2, distancia):
	print(f"La distancia entre el punto {punto1} y el punto {punto2} es de {distancia}")

punto1, punto2, x1, y1, x2, y2 = valores()

distancia = procedimiento(x1, y1, x2, y2)

salida(punto1, punto2, distancia)