orden = 5

matriz = []

#Este bucle permite crear una matriz 5x5 y rellenarla con numeros uno.

for f in range(orden):
	matriz.append([])
	for c in range(orden):
		numero = 1
		matriz[f].append(numero)


#Este ciclo permite llenar de ceros toda la matriz menos el borde completo.

for f in range(1, orden-1):
	for c in range(1, orden-1):
		matriz[f][c] = 0

print()

for i in matriz:
	print(i)