

nombres = []
generos = []
edades = []

cantidadPersonas = int(input("Ingrese la cantidad de personas: "))

for i in range(cantidadPersonas):
	nombre = input("Ingrese el nombre: ").upper()
	nombres.append(nombre)
	genero = input("Ingrese el genero femenino/masculino: ").upper()
	generos.append(genero)
	edad = int(input("Ingrese la edad: "))
	edades.append(edad)


#print(nombres)
#print(generos)
#print(edades)

cantidadMasculinos = 0

for f in generos:
	
	if f == "MASCULINO":
		cantidadMasculinos = cantidadMasculinos + 1

print(f"La cantidad de individuos masculinos es de {cantidadMasculinos}")

cantidadFemMayor = 0

for f in range(cantidadPersonas):
	if generos[f] == "FEMENINO" and edades[f] >= 18:
		cantidadFemMayor = cantidadFemMayor + 1

print(f"La cantidad de mujeres que superan la mayoría de edad es de {cantidadFemMayor}")

sumaEdadHombres = 0

for f in range(cantidadPersonas):
	if generos[f] == "MASCULINO":
		sumaEdadHombres = sumaEdadHombres + edades[f]

#print(sumaEdadHombres)

promedioEdadMasculino = 0

if cantidadMasculinos != 0:
	promedioEdadMasculino  = sumaEdadHombres / cantidadMasculinos

print(f"El promedio de edad de los hombres es de {promedioEdadMasculino}")

numPeq = 99

for f in range(cantidadPersonas):
	if generos[f] == "FEMENINO":
		if edades[f] < numPeq:
			numPeq = edades[f]

#print(numPeq)

nombreMasJoven = "N/A"

for f in range(cantidadPersonas):
	if edades[f] == numPeq:
		nombreMasJoven = nombres[f]

print(f"La mujer más joven es {nombreMasJoven}")