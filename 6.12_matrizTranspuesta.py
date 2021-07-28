matriz = []

numeroFilas = int(input("Ingrese el número de filas: "))
numeroColumnas = int(input("Ingrese el número de columnas: "))

#A continuación se crea una matriz ingresando los datos a cada celda

for f in range(numeroFilas):
	matriz.append([])
	for c in range(numeroColumnas):
		numero = int(input(f"Ingrese un número para el dato ({f}, {c}): "))
		matriz[f].append(numero)

print()
print("Matriz Original")
print()
for i in matriz:
	print(i)

print()

print("Matriz Transpuesta:")

print()

#se crea una nueva matriz donde las filas de la original serán las columnas de la nueva matriz y las columnas
#de la orignal serán las filas de la nueva matriz

#La nueva matriz dependera de la relación entre numeroFilas y numeroColumnas

matriz2 = []


if numeroFilas == numeroColumnas:

	for j in range(numeroFilas):
		matriz2.append([])
		for k in range(numeroColumnas):
			matriz2[j].append(matriz[k][j])

	for l in matriz2:
		print(l)

if numeroFilas < numeroColumnas:

	for j in range(numeroColumnas):
		matriz2.append([])
		for k in range(numeroFilas):
			matriz2[j].append(matriz[k][j])

	for l in matriz2:
		print(l)

if numeroFilas > numeroColumnas:

	for j in range(numeroColumnas):
		matriz2.append([])
		for k in range(numeroFilas):
			matriz2[j].append(matriz[k][j])

	for l in matriz2:
		print(l)