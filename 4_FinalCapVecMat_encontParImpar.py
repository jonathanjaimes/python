cantNum = int(input("Ingrese la cantidad de números a almacenar: "))



arreglo1 = []

#Este ciclo permite agregar numeros pares e impares al arreglo1

for i in range(cantNum):
	while True:
		numero = int(input(f"Ingrese el número {i+1}: "))
		if numero >= 50 and numero <= 100:
			break
	arreglo1.append(numero)

print(arreglo1)

pares = []

impares = []

#Este ciclo permite agregar los numeros pares al arreglo de pares y lo mismo con impares

for i in range(cantNum):
	if arreglo1[i] % 2 == 0:
		pares.append(arreglo1[i])

	else:
		impares.append(arreglo1[i])

print(f"Los números pares son:")
print(pares)
print()
print(f"Los números impares son:")
print(impares)