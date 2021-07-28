cantidadNum = int(input("Ingrese la cantidad de números enteros a ingresar: "))
sumaCantidad = 0

listaNum = []

while sumaCantidad < cantidadNum:
	numero = int(input("Ingrese el número: "))
	listaNum.append(numero)
	sumaCantidad = sumaCantidad + 1

print(listaNum)

def pares():
	sumaPares = 0
	for i in range(0, len(listaNum)):
		result  = listaNum[i]%2
		if result == 0:
			sumaPares = sumaPares + 1
	return sumaPares

sumaPares = pares()

print(f"La cantidad de números pares es {sumaPares}")
print(f"La cantidad de números impares es {len(listaNum)-sumaPares}")