saldoBase = float(input("Ingrese el saldo base: "))
sumaIngresos = 0
sumaEgresos = 0
while True:

	operacion = input("Desea registrar un ingreso o un egreso? i/e (Digite x para salir): ")

	operacion = operacion.upper()

	
	if operacion == "I":
		cantidadIngreso = float(input("Ingrese la cantidad: "))
		saldoBase = saldoBase + cantidadIngreso
		sumaIngresos = sumaIngresos + cantidadIngreso

	elif operacion == "E":
		cantidadEgreso = float(input("Ingrese la cantidad: "))
		saldoBase = saldoBase - cantidadEgreso
		sumaEgresos = sumaEgresos + cantidadEgreso

	elif operacion == "X":
		break

	else:
		print("Opción inválida")

	print(f"El saldo en caja es de: {saldoBase}")

print(f"El saldo en caja es de {saldoBase}")
print(f"Los ingresos fueron de {sumaIngresos}")
print(f"Los ingresos fueron de {sumaEgresos}")