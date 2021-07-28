def limites():
	a = int(input("Ingrese un valor a: "))
	while True:
		b = int(input("Ingrese un valor b mayor que a: "))
		if a < b:
			break
	while True:
		c = int(input("Ingrese un valor c mayor que b: "))
		if b < c:
			break
	while True:	
		d = int(input("Ingrese un valor d mayor que c: "))
		if c < d:
			break
	while True:	
		e = int(input("Ingrese un valor e mayor que d: "))
		if d < e:
			break
	while True:	
		f = int(input("Ingrese un valor f mayor que e: "))
		if e < f:
			break
	return a, b, c, d, e, f

a, b, c, d, e, f = limites()

def entradaValor():
	n = int(input("Ingrese un número: "))
	return n

n = entradaValor()

def rango(a, b, c, d, e, f, n):
	if n > a and n < b:
		print(f"El número {n} se encuentra en el intervalo ({a}, {b})")
	elif n > c and n < d:
		print(f"El número {n} se encuentra en el intervalo ({c}, {d})")
	elif n > e and n < f:
		print(f"El número {n} se encuentra en el intervalo ({e}, {f})")
	else: 
		print(f"El número {n} no se encuentra en ningún intervalo")

rango(a, b, c, d, e, f, n)