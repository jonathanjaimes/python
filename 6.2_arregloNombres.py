cantidad = int(input("Cuantos nombres quiere almacenar: "))

listaNombres = []

sumaCantidad = 0

#El while permite agregar tantos nombres como se haya especificado en el apartado cantidad.

while sumaCantidad < cantidad:

	nombre = input(f"Ingrese el nombre {sumaCantidad}: ")
	listaNombres.append(nombre)

	sumaCantidad = sumaCantidad + 1

preguntaNombre = input("Ingrese el nombre del que desea saber la posición: ")

bandera = False

#Este for va a comparar cada elemento de la lista con el nombre preguntado. En caso de hallar alguna coincidencia, 
#la bandera cambiará el estado a True

for i in range(0, len(listaNombres)):
	if listaNombres[i] == preguntaNombre:
		posicion = i
		bandera = True

#Esta condición permite imprimir un mensaje indicando el indice del elemento buscado solo si el estado de bandera es verdadero,
#de lo contrario, imprimirá un mensaje avisando que el elemento no se encuentra en la lista.

if bandera == True:
	print(f"La posición de {preguntaNombre} es {posicion}")

else: 
	print(f"El nombre {preguntaNombre} no se encuentra en la lista")