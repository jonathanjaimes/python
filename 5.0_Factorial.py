numero = int(input("Ingrese un número: "))

def facto(numero):
	contador = numero-1
	factorial = numero

	while contador != 0:
		factorial = factorial * contador
		#print(contador)
		contador = contador - 1

	return factorial
	
factor = facto(numero)

print(f"El factorial de {numero} es {factor}")