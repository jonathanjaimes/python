fila1 = 1
fila2 = 1
fila3 = 2

n = int(input("Ingrese la cantidad de términos: "))

for i in range(0, n*2, 2):
	print(fila1, fila2, fila3)
	fila1 = fila1 + 1 
	fila2 = fila2 + 3 + i
	fila3 = fila3 + 4 + i