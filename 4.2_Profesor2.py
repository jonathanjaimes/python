contador = 0
contador1 = 0
contador2 = 0
acumuladorNotas = 0
repeticiones = int(input("Ingrese la cantidad de alumnos a ingresar: "))

while contador < repeticiones:
	contador = contador + 1
	nota = float(input("Ingrese nota: "))
	acumuladorNotas = acumuladorNotas + nota
	if nota >= 3.0:
		contador1 = contador1 + 1
	
	elif nota < 3.0:
		contador2 = contador2 + 1 

promedio = acumuladorNotas/repeticiones
print(f"La cantidad de alumnos que aprobaron fue de: {contador1}")
print(f"La cantidad de alumnos que repobaron fue de: {contador2}")
print(f"El promedio de las notas es de: {promedio}")

