cantidad = int(input("Ingrese la cantidad de números a ingresar: "))

listaNumeros1 = []

listaNumeros2 = []

suma = 0

#Se van a ingresar tantos elementos a la lista como unidades haya en la variable cantidad.

while suma < cantidad:
	numero = int(input("Ingrese un número: "))
	listaNumeros1.append(numero)

	suma = suma + 1

print(listaNumeros1)

#se va a hacer un recorrido inverso de la lista, y para cada elemento, este se agrega a la segunda lista.

for i in range(len(listaNumeros1)-1, -1, -1):
	numero2 = listaNumeros1[i]
	listaNumeros2.append(numero2)

print(listaNumeros2)