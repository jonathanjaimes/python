numeroFilas = int(input("Ingrese el número de filas de la matriz: "))
numeroColumnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz = []

for f in range(numeroFilas):
	matriz.append([])
	for c in range(numeroColumnas):
		while True:
			numero = int(input("Ingrese un número entre 50 y 100: "))
			if numero >= 50 and numero <= 100:
				break
		matriz[f].append(numero)


for i in matriz:
	print(i)

print()

numeroBuscar = int(input("Ingrese el número a buscar: "))

numeroEncontrado = ""

for f in range(numeroFilas):
	for c in range(numeroColumnas):
		if matriz[f][c] == numeroBuscar:
			numeroEncontrado = matriz[f][c]
			a = f + 1
			b = c + 1

if numeroEncontrado != "":
	print(f"El número a sido encontrado y se encuentra en la fila {a} y columna {b}")

else:
	print("El número buscado no se encuentra en la matriz")