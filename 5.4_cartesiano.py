def letra():
	letra = input("Ingrese el nombre del punto: ")
	return letra

def tomarCoord(a):
	x = int(input(f"Ingresar la coordenada X en en el punto {a}: "))
	y = int(input(f"Ingresar la coordenada Y en en el punto {a}: "))
	return x, y

def imprimirCoord(a, b, c):
	print(f"Las coordenadas del punto {a} son ({b}, {c})")

contador = 0
while contador <= 2:
	caracter = letra()

	coord1, coord2 = tomarCoord(caracter)

	imprimirCoord(caracter, coord1, coord2)

	contador = contador + 1 

