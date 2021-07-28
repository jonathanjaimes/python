while True:
	cantidadPersonas = int(input("Ingrese la cantidad de personas: "))
	if cantidadPersonas <= 500:
		break

contMenores = 0
contMayores = 0
for x in range(1, cantidadPersonas+1):
	edad = int(input(f"Ingrese la edad de la persona {x}: "))
	if edad < 18:
		contMenores = contMenores + 1
	else:
		contMayores = contMayores + 1

if contMayores == 1:
	plural = "es mayor"
else:
	plural = "son mayores"
print(f"La cantidad total de personas es de {cantidadPersonas}, de ellas, {contMenores} son menores de edad y {contMayores} {plural} de edad.")