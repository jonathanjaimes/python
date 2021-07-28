cantidadPersonas = int(input("Ingrese la cantidad de personas a registrar: "))

listaGenero = []

listaEstatura = []

#Se agrega mediante un recorrido los elementos a las listas correspondientes

for i in range(0, cantidadPersonas):
	genero = input(f"Ingrese el género de la persona {i+1}: ")
	genero = genero.upper()
	listaGenero.append(genero)

	estatura = float(input(f"Ingrese la estatura de la persona {i+1}: "))
	listaEstatura.append(estatura)

#Mediante esta función se halla la suma de las estaturas de todas las mujeres ingresadas

def promedio():
	sumaEstatura = 0
	for i in range(0, len(listaGenero)):
		if listaGenero[i] == "FEMENINO":
			sumaEstatura = sumaEstatura + listaEstatura[i]

	return sumaEstatura

sumaEstatura = promedio()

#Mediante esta función se haya la cantidad de hombres ingresados

def porcentaje():
	sumaHombres = 0
	for i in range(0, len(listaGenero)):
		if listaGenero[i] == "MASCULINO":
			sumaHombres = sumaHombres + 1
	return sumaHombres

sumaHombres = porcentaje()

#Se haya el porcentaje que representa el total de hombres ingresados
porcentajeHombres = (sumaHombres * 100) / cantidadPersonas

#Se realiza el promedio con el total de estaturas de las mujeres ingresadas
estaturaPromedio = sumaEstatura / (cantidadPersonas - sumaHombres)

print(f"El promedio de estatura de las mujeres es de {estaturaPromedio} metros")
print(f"El porcentaje de hombres es de {porcentajeHombres}%")