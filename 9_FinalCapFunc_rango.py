def entradaExtremos():
	while True:
		a = int(input("Ingrese un valor: "))
		b = int(input("Ingrese un valor mayor que el anterior: "))
		if a < b:
			break
	return a, b

a, b = entradaExtremos()

def entradaDato():
	n = int(input("Ingrese un número: "))
	return n

n = entradaDato()

def rango(a, b, n):
	if n >= a and n <= b:
		print(f"El valor {n} está dentro del rango [{a}, {b}]")
	else:
		print(f"El valor {n} NO está dentro del rango [{a}, {b}]")
rango(a, b, n)