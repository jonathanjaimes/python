while True:	
	while True:

		n = int(input("Ingrese un número: "))
		if n > 1:
			break

	numero = n-1
	contador = 0

	while numero != 0:
		
	    mod = n%numero

	    if mod == 0:
	        contador = contador + numero

	    numero = numero-1

	if contador == n:
		print(f"El número {n} es un número perfecto")

	else:
		print(f"El número {n} NO es perfecto")

	opcion = input("Desea salir si/no: ")
	opcion = opcion.upper()

	if opcion == "SI":
		break