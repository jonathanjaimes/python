matriz = []

orden = int(input("Introduce el orden de la matriz: "))

for f in range(orden):
    matriz.append([])
    for c in range(orden):
        dato = int(input(f"Introduce el número para la celda ({f}, {c}): "))
        matriz[f].append(dato)
for f in matriz:
    print(f)


c = 0

f = 0

suma = matriz[f][c]

for f in range(1, orden):
    c = c+1
    suma = suma + matriz[f][c]

#print(suma)

#############################################################
#El anterior código encuentra la suma de la diagonal principal

c = orden-1

f = 0


suma2 = matriz[f][c]

for f in range(1, orden):
    c = c-1
    suma2 = suma2 + matriz[f][c]

#print(suma2)

#El código anterior haya la suma de la diagonal secundaria.

if suma == suma2:
	print("La suma de los elementos de la diagonal principal y la secundaria son iguales")
elif suma > suma2:
	print("La suma de la diagonal principal es mayor a la suma de la diagonal secundaria")
else:
	print("La suma de la diagonal secundaria es mayor a la suma de la diagonal principal")