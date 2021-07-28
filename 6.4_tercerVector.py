
cantidadPares = int(input("Escriba la cantidad de números pares que desea ingresar: "))

sumaPares = 0

listaPares = []

while sumaPares < cantidadPares: 
	while True:
		numerosPares = int(input("Ingrese un número par: "))
		if numerosPares%2 == 0:
			break

	listaPares.append(numerosPares)

	sumaPares = sumaPares + 1

print(listaPares)



cantidadImpares = int(input("Escriba la cantidad de números impares que desea ingresar: "))

sumaImpares = 0

listaImpares = []

while sumaImpares < cantidadImpares: 
	while True:
		numerosImpares = int(input("Ingrese un número impar: "))
		if numerosImpares%2 != 0:
			break

	listaImpares.append(numerosImpares)

	sumaImpares = sumaImpares + 1

print(listaImpares)


listaTotal = []


for i in range(0, cantidadPares):
	numPar = listaPares[i]
	listaTotal.append(numPar)

for j in range(0, cantidadImpares):
	numImpar = listaImpares[j]
	listaTotal.append(numImpar)

print(f"La lista que contiene las dos listas anteriores contiene: {listaTotal}")