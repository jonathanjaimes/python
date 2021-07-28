"""
numero = int(input("Ingrese la cantidad de términos que quiere: "))
contador = 1
contadorTerminos = 0
while True:
	print(contador)
	contador = contador + 2 
	contadorTerminos = contadorTerminos+1
	if contadorTerminos == numero:
		break

"""

cantidad = int(input("Ingrese la cantidad de números: "))
contador = 0
termino = 1
while contador < cantidad - 1:
	print(termino)
	termino = termino + 2
	contador = contador + 1