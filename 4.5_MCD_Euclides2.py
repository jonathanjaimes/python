#ciclo repita

while True:
	
	#Ingreso de los dos números a los cuales se les va a encontrar el MCD y el mcm.

	a = int(input("Ingrese el mayor de los dos números: "))
	b = int(input("Ingrese el menor de los dos números: "))

	copiaA = a
	copiaB = b

	#formula para hallar el residuo

	c= copiaA % copiaB

	while c != 0:
	    copiaA = copiaB
	    copiaB = c
	    c= copiaA % copiaB


	print(f"El MCD de los numeros {a} y {b} es {copiaB}")

	mcm = (a*b)//copiaB

	print(f"El mcm de los números {a} y {b} es {mcm}")
	print()

	eleccion = input("Ingrese 's' para continuar y 'n' para salir: ")
	print()
	if eleccion == "n":
		break