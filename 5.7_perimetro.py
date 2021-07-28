
#En esta primera función se ingresan los datos necesarios.

def tomaDatos():
	punto1 = input("Ingrese el nombre del primer punto: ")
	x1 = float(input(f"Ingrese la primera coordenada del punto {punto1}: "))
	y1 = float(input(f"Ingres la segunda coordenada del punto {punto1}: "))
	punto2 = input("Ingrese el nombre del primer punto: ")
	x2 = float(input(f"Ingrese la primera coordenada del punto {punto2}: "))
	y2 = float(input(f"Ingres la segunda coordenada del punto {punto2}: "))
	punto3 = input("Ingrese el nombre del primer punto: ")
	x3 = float(input(f"Ingrese la primera coordenada del punto {punto3}: "))
	y3 = float(input(f"Ingres la segunda coordenada del punto {punto3}: "))
	return punto1, punto2, punto3, x1, y1, x2, y2, x3, y3

#En esta segunda función, realizamos las operaciones respectivas.

def distancia(x1, x2, x3, y1, y2, y3):
	distancia1 = (((x2-x1)**2) + ((y2-y1)**2))**(1/2)
	distancia2 = (((x3-x2)**2) + ((y3-y2)**2))**(1/2)
	distancia3 = (((x3-x1)**2) + ((y3-y1)**2))**(1/2)
	distanciaTotal = distancia1 + distancia2 + distancia3
	return distanciaTotal

#En esta última función se imprimen los resultados obtenidos a partir de la segunda función.

def salida(x1, x2, x3, y1, y2, y3, punto1, punto2, punto3, distanciaTotal):
	print(f"La distancia entre los puntos {punto1}, {punto2}, {punto3} es {distanciaTotal}")

punto1, punto2, punto3, x1, y1, x2, y2, x3, y3 = tomaDatos()

distanciaTotal = distancia(x1, x2, x3, y1, y2, y3)

salida(x1, x2, x3, y1, y2, y3, punto1, punto2, punto3, distanciaTotal)