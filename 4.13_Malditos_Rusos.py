while True:

	a = int(input("Ingrese un número: "))
	b = int(input("Ingrese otro número: "))

	if a >= 0 and a <= 10000 and b >= 0 and b <= 10000:
		break

a2 = a
b2 = b

sumar = 0

while True:



	if b%2 != 0:
		sumar = sumar + a
	
	a = a*2
	b = b//2

	if b < 1:
		break

	

print(f"El producto de {a2} y {b2} es {sumar}")
