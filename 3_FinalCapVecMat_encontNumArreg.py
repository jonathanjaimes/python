cantidadNum = int(input("Ingrese la cantidad de números a almacenar: "))

arreglo = []

#Este ciclo permite almacenar los números en el arreglo

for i in range(cantidadNum):
	numero = int(input(f"Ingrese el número {i}: "))
	arreglo.append(numero)

print(arreglo)

numBusc = int(input("Ingrese el número a buscar: "))

clave = 0

#Este ciclo permite buscar un número en el arreglo y guardar su posicion. Si encuentra al número
#clave será distinto de cero.

for i in range(cantidadNum):
	if numBusc == arreglo[i]:
		posicion = i
		clave = clave + 1

if clave != 0:
	print(f"El número a sido encontrado y se encuentra en la posición {posicion}")

else:
	print("El número no se encuentra en el arreglo")