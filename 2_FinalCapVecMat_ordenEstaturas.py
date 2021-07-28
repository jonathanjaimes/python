
nombres = []

estaturas = []

#Permite ingresar los datos a las tres listas

cantidadPersonas = int(input("Ingrese la cantidad de personas: "))

for i in range(cantidadPersonas):
	nombre = input(f"Ingrese el nombre de la persona {i}: ")
	nombres.append(nombre)
	estatura = float(input(f"Ingrese la estatura de la persona {i}: "))
	estaturas.append(estatura)

#print(nombres)
#print(estaturas)


#estaturas = [4, 3, 6, 2, 1, 8, 7]

#ordena la lista estaturas y nombres de menor a mayor

cont = len(estaturas)

while True:
    for f in range(len(estaturas)-1):
        if estaturas[f] > estaturas[f+1]:
            a = estaturas[f]
            b = estaturas[f+1]

            c = nombres[f]
            d = nombres[f+1]

            estaturas[f] = b
            estaturas[f+1] = a
            
            nombres[f] = d
            nombres[f+1] = c
    
    #for f in range(len(lista)-1):
     #   if lista[f] > lista[f+1]:
            
    cont = cont - 1

    if cont == 0:
        break

#Imprime las estaturas y los nombres ordenados de menor a mayor

print()
print("Estaturas de menor a mayor")
print()
print(estaturas)
print(nombres)

#Ordena la lista estaturas y nombres de mayor a menor

cont = len(estaturas)

while True:
    for f in range(len(estaturas)-1):
        if estaturas[f] < estaturas[f+1]:
            a = estaturas[f]
            b = estaturas[f+1]

            c = nombres[f]
            d = nombres[f+1]

            estaturas[f] = b
            estaturas[f+1] = a
            
            nombres[f] = d
            nombres[f+1] = c
    
    #for f in range(len(lista)-1):
     #   if lista[f] > lista[f+1]:
            
    cont = cont - 1

    if cont == 0:
        break

#Imprime las estaturas y los nombres ordenados de mayor a menor

print()
print("Estaturas de mayor a menor")
print()
print(estaturas)
print(nombres)