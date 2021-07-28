

orden = 5

matriz = []

for f in range(orden):
	matriz.append([])
	for c in range(orden):
		numero = int(input(f"Ingrese el número de la celda ({f}, {c}): "))
		matriz[f].append(numero)

for i in matriz:
	print(i)

"""
matriz = [[1,2,3], [4,5,6], [7,8,9]]

for i in matriz:
	print(i)
"""

for c in range(4, -1, -1):
	print()
	for f in range(4, -1, -1):
		print(matriz[f][c])