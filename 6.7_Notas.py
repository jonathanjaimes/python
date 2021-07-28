listaNotas = []

notaMenor = 5
notaMayor = 0

for i in range(1, 21):
	nota = float(input(f"Ingrese la nota final {i}: "))
	listaNotas.append(nota)
	if nota < notaMenor:
		notaMenor = nota

	if nota > notaMayor:
		notaMayor = nota

def promedioNotas():
	sumaNotas = 0
	for i in range(0, len(listaNotas)):
		sumaNotas = sumaNotas + listaNotas[i]

	promedio = sumaNotas / len(listaNotas)
	return promedio

promedioNotas = promedioNotas()

print(f"El promedio de las notas ingresadas es {promedioNotas}")
print(f"La mayor nota fue {notaMayor}")
print(f"La menor nota fue {notaMenor}")