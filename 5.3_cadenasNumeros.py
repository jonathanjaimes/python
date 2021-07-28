numero = int(input("Ingrese el número de términos: "))
print()

def secuencia1(n):

	for i in range(1, n+1):
		producto = 3*i
		print(producto, end=" ")

secuencia1(numero)
print()
print()

def secuencia2(n):

	for i in range(1, n+1):
		producto = 5*i
		print(producto, end=" ")

secuencia2(numero)
print()