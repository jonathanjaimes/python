
contador = 0
contador2 = 0

while True:
	nota = float(input("Ingrese nota: "))
	salir = input("Ver total aprobados s/n: ")
	if nota >= 3.0:
		contador = contador + 1
	
	elif nota < 3.0:
		contador2 = contador2 + 1 

	if salir == "s":
		break

print(f"La cantidad de alumnos que aprobaron fue de: {contador}")
print(f"La cantidad de alumnos que repobaron fue de: {contador2}")

