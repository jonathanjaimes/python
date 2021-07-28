#matriz1 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19]]

matriz1 = []

#Este bucle permite crear una matriz 4x5

for f in range(2):
	matriz1.append([])
	for c in range(3):
		numero = int(input(f"Ingrese número para la celda ({f}, {c}): "))
		matriz1[f].append(numero)

for i in matriz1:
	print(i)

print()
print("Matriz transpuesta:")
print()
matrizTrans = []

#Este bucle permite crear una matriz transpuesta partiendo de la matriz original

for c in range(3):
	matrizTrans.append([])
	for f in range(2):
		
		matrizTrans[c].append(matriz1[f][c])

for i in matrizTrans:
	print(i)