while True:
	while True:
		n = int(input("Quiero practicar con la tabla del: "))
		if n <= 20:
			break
	contador = 0
	for i in range(1, 11): 
		producto = n * i
		resultado = int(input(f"{n} por {i} es igual a: "))
		if producto == resultado:
			print("Felicitaciones")
			contador = contador + 1
		else:
			print("Respuesta incorrecta")

	if contador <= 5:
		print("Su desempeño fue Insuficiente")
	elif contador >= 6 and contador <= 7:
		print("Su desempeño fue aceptable")
	elif contador >= 8 and contador <= 9:
		print("Su desempeño fue sobresaliente")
	else:
		print("Su desempeño fue excelente")

	cont = input("¿Desea continuar? si/no: ")
	cont = cont.upper()

	if cont == "NO":
		break