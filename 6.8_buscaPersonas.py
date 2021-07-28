cantidadPersonas = int(input("Ingrese la cantidad de personas a almacenar: "))

listaPersonas = []

for i in range(0, cantidadPersonas):
	nombre = input(f"Ingree el nombre de la persona {i+1}: ")
	genero = input(f"Ingrese el género de la persona {i+1}: ")
	nombre = nombre.upper()
	genero = genero.upper()
	listaPersonas.append(nombre)
	listaPersonas.append(genero)

print(listaPersonas)

def buscar():
	buscNom = input("Qué nombre desea buscar?: ")
	buscGen = input("Qué género desea buscar? ")
	buscNom = buscNom.upper()
	buscGen = buscGen.upper()

	posicion = ""

	for i in range(0, len(listaPersonas)):
		if buscNom == listaPersonas[i]:
			if buscGen == listaPersonas[i+1]:
				posicion = (listaPersonas.index(buscGen))-1
	return posicion
	
posicion =  buscar()

if posicion == "":
	print("No se ha encontrado el registro buscado")
else:
	print(f"La posición del registro buscado es {posicion}")