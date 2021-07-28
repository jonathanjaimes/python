
numero = 1
contador = 0
#n = int(input("Por favor, ingrese la cantidad de números de la serie: "))
cantidadTerminos = int(input("Ingrese numero: "))
cantidadTerminos = cantidadTerminos*2
while numero <= cantidadTerminos:
	contador = contador + 1
	print(numero, contador)
	numero = numero + 2 



numero = 1
cantidadTerminos = int(input("Ingrese numero: "))
contadorNumeros = 0
while contadorNumeros <= (cantidadTerminos - 1):
	contadorNumeros = contadorNumeros + 1
	print(numero, contadorNumeros)
	numero = numero + 2 
	