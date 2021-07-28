

numero = int(input("Ingrese el número: "))
acumulador = 0
cont = 0
if numero >= 0:
	
	while numero != 0:
		ultimaCifra = numero % 10
		acumulador = acumulador + ultimaCifra
		numero = numero // 10
		cont = cont + 1

	print(acumulador)
	print(cont)
else:
	print("El número ingresado no es positivo.")