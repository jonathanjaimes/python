cantidadPersonas = int(input("Ingrese el número de personas que va a registrar: "))

listaNombre = []

listaGenero = []

for i in range(0, cantidadPersonas):
	nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
	nombre = nombre.upper()
	listaNombre.append(nombre)
	genero = input(f"Ingrese el género de la persona {i+1}: ")
	genero = genero.upper()
	listaGenero.append(genero)

def buscar():

	buscNom = input("Ingrese el nombre que desea buscar: ")
	buscNom = buscNom.upper()
	posicion = ""
	for i in range(0, len(listaNombre)):
		if buscNom == listaNombre[i]:
			posicion = listaNombre.index(buscNom)

	return posicion

posicion = buscar()



if posicion == "":
	print("El nombre buscado no está en el registro")

else:
	generoEncontrado = listaGenero[posicion]
	print(f"El nombre buscado tiene la posicion {posicion} y su género es {generoEncontrado}")