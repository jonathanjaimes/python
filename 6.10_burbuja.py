listaNumeros = []

#este recorrido permite ingresar 4 números

for i in range(0, 4):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    listaNumeros.append(numero)

print("Los números ingresados son: ")
print(listaNumeros)
print()

#Esta función ordena por metodo burbuja hasta que se cumpla la condicion
#de que todos estan ordenados de menor a mayor

def burbuja():

	while True:

	    for i in range(0, len(listaNumeros)-1):
	            
	        while listaNumeros[i] > listaNumeros[i+1]:
	            a = listaNumeros[i]
	            b = listaNumeros[i+1]
	                    
	            listaNumeros[i] = b
	            listaNumeros[i+1] = a 
	    
	    if listaNumeros[0] <= listaNumeros[1] and listaNumeros[1] <= listaNumeros[2] and listaNumeros[2] <= listaNumeros[3]:
	        break

	return listaNumeros

listaNumeros = burbuja()

print("Los números en orden ascendente son: ")
print(listaNumeros)