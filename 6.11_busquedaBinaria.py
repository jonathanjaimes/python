listaNumeros = []

cantidadNumeros = int(input("Ingrese la cantidad de números a guardar: "))

#este recorrido permite ingresar 4 números

for i in range(0, cantidadNumeros):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    listaNumeros.append(numero)

#print("Los números ingresados son: ")
#print(listaNumeros)
#print()

#Esta función ordena por metodo burbuja hasta que se cumpla la condicion
#de que todos estan ordenados de menor a mayor

def burbuja():

	sumaWhile = 0
	while sumaWhile < len(listaNumeros)**2:

	    for i in range(0, len(listaNumeros)-1):
	            
	        while listaNumeros[i] > listaNumeros[i+1]:
	            a = listaNumeros[i]
	            b = listaNumeros[i+1]
	                    
	            listaNumeros[i] = b
	            listaNumeros[i+1] = a 
	    
	    sumaWhile = sumaWhile +1
	    #if listaNumeros[0] <= listaNumeros[1] and listaNumeros[1] <= listaNumeros[2] and listaNumeros[2] <= listaNumeros[3]:
	        #break

	return listaNumeros

listaNumeros = burbuja()

print("Los números en orden ascendente son: ")
print(listaNumeros)

#El siguiente algoritmo permite hacer la búsqueda binaria partiendo del arreglo ordenado de números.

numeroBuscar = int(input("Ingrese el número a buscar: "))

a = 0
b = len(listaNumeros) - 1



bandera = False

while True:

    m = (a+b)//2

    if listaNumeros[m] < numeroBuscar:
        a = m+1

    elif listaNumeros[m] > numeroBuscar:
        b = m-1

    else:
        bandera = True
        print(f"El número ha sido encontrado, su posición es {listaNumeros.index(listaNumeros[m])}")

    if bandera == True:
        break