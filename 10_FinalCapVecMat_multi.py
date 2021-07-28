#El número de columnas = número de filas
"""
matrizA = [[1,2,3],[4,5,6]]

matrizB = [[1,2,4,5],[3,4,4,5],[5,6,4,5]]



#para que se pueda multiplicar, columnasA == filasB

filasA = 2
columnasA = 3

filasB = 3
columnasB = 4

"""

filasA = int(input("Ingrese la cantidad de filas de la matriz A: "))
columnasA = int(input("Ingrese la cantidad de columnas de la matriz A: "))
print()
filasB = int(input("Ingrese la cantidad de filas de la matriz B: "))
columnasB = int(input("Ingrese la cantidad de columnas de la matriz B: "))

matrizA = []
matrizB = []

#Estos dos bucles permiten crear las dos matrices que se van a multiplicar

for f in range(filasA):
	matrizA.append([])
	for c in range(columnasA):
		numero = int(input(f"Ingrese para matriz A el número de la celda ({f}, {c}): "))
		matrizA[f].append(numero)

for f in range(filasB):
	matrizB.append([])
	for c in range(columnasB):
		numero = int(input(f"Ingrese para matriz B el número de la celda ({f}, {c}): "))
		matrizB[f].append(numero)



for i in matrizA:
	print(i)

print()

for i in matrizB:
	print(i)

#la matriz resultante será 2x2


print()
print("Matriz transpuesta:")
print()
matrizTrans = []

#Este bucle permite crear una matriz transpuesta partiendo de la matriz original

for c in range(columnasB):
	matrizTrans.append([])
	for f in range(filasB):
		
		matrizTrans[c].append(matrizB[f][c])

for i in matrizTrans:
	print(i)

matrizPro = []

#Este bucle permite multiplicar cada elemento de la primera fila de la primera matriz, por cada elemento
#de cada una de las filas de la matriz transpuesta de la segunda matriz sumando los productos de cada
#fila de la transpuesta y almacenándolos en una nueva matriz.

for f in range(filasA):
	matrizPro.append([])
	for i in range(columnasB):
		suma = 0
		for c in range(filasB):
			numero = matrizA[f][c] * matrizTrans[i][c]
			suma = suma + numero
		matrizPro[f].append(suma)

print()
print("Matriz producto")
print()
for h in matrizPro:
	print(h)