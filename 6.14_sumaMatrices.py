matriz1 = []

matriz2 = []

matriz3 = []

#Realizamos la primera matriz

print()
print("Primera matriz")
print()

for f in range(3):
	matriz1.append([])
	for c in range(3):
		numero1 = int(input(f"Ingrese el dato para el espacio ({f}, {c}): "))
		matriz1[f].append(numero1)

#imprimimos la primera matriz

for i in matriz1:
	print(i)

#Realizamos la segunda matriz

print()
print("Segunda matriz")
print()

for f in range(3):
	matriz2.append([])
	for c in range(3):
		numero2 = int(input(f"Ingrese el dato para el espacio ({f}, {c}): "))
		matriz2[f].append(numero2)

#Imprimimos la segunda matriz

for i in matriz2:
	print(i)

#Realizamos la tercera matriz, que contendrá la suma se los elementos de las dos matrices anteriores.

print()
print("Tercera matriz")
print()

for f in range(3):
	matriz3.append([])
	for c in range(3):
		numeroSuma = matriz1[f][c] + matriz2[f][c]
		matriz3[f].append(numeroSuma)

#imprimimos la tercera matriz

for i in matriz3:
	print(i)