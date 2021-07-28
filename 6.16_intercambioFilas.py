def mat():

	matriz1 = []

	numeroFilas = int(input("Ingrese el número de filas: "))
	numeroColumnas = int(input("Ingrese el número de columnas: "))

	for f in range(numeroFilas):
		matriz1.append([])
		for c in range(numeroColumnas):
			caracter = input(f"Ingrese el caracter para la celda ({f}, {c}): ")
			matriz1[f].append(caracter)

	return matriz1

matrizA = mat()

for f in matrizA:
	print(f)

#Elegimos los elementos que vamos a intercambiar

print("Introduce la posición de la fila y la columna del primer elemento que deseas cambiar")

a = int(input("Introduce la fila del primer elemento: "))

b = int(input("Introduce la columna del primer elemento: "))

print("Introduce la posición de la fila y la columna del segundo elemento que deseas cambiar")

c = int(input("Introduce la fila del primer elemento: "))

d = int(input("Introduce la columna del primer elemento:"))

#duplicamos la matrizA en una nueva matrizB

matrizB = matrizA

#Guardamos los elementos que seleccionamos en variables separadas

elemento1 = matrizA[a][b]
elemento2 = matrizA[c][d]

#En la nueva matriz intercambiamos los elementos de lugar

matrizB[a][b] = elemento2
matrizB[c][d] = elemento1

for f in matrizB:
	print(f)