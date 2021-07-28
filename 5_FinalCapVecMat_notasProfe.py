cantidadEst = int(input("Ingrese la cantidad de estudiantes: "))

nombres = []

matrizNotas = []

#Permite agregar en primer lugar, tantas listas como estudiantes haya y en segundo lugar,
#permite ingresar las cinco notas a las listas creadas por cada estudiante.

for f in range(cantidadEst):
	matrizNotas.append([])
	nombre = input(f"Ingrese el nombre del estudiante {f+1} ")
	nombres.append(nombre)
	for c in range(5):
		nota = float(input(f"Ingrese la nota {c+1} del estudiante {f+1}: "))
		matrizNotas[f].append(nota)

print()
print("Nombres")
print(nombres)
print()

for i in matrizNotas:
	print(i)

promedios = []

#Este ciclo permite hayar los promedios de notas por cada estudiantes y almacenarlos en una nueva lista promedios.

for f in range(cantidadEst):
	sumaNotas = 0
	for c in range(5):
		sumaNotas = sumaNotas + matrizNotas[f][c]

	promedio = sumaNotas / 5

	promedios.append(promedio)

print()
print("Nombres promedio")
print(promedios)
print()

notaMayor = 0

#Este bucle permite conocer la nota mayor, su indice y con el, conocer el nombre del estudiante
#al que pertenece esa nota mayor.

for i in range(cantidadEst):
	if promedios[i] > notaMayor:
		notaMayor = promedios[i]
		indexNotaMayor = i

print(f"El estudiante con mejor promedio es {nombres[indexNotaMayor]}")

print()

nomPerMat = []

notaPerMat = []

#Este bucle permite escoger todos los estudiantes con notas promedio menores a 2.0 y 
#guardarlos en una lista.

for i in range(cantidadEst):
	if promedios[i] < 2:
		nomPerMat.append(nombres[i])
		notaPerMat.append(promedios[i])

print("Estudiantes que han perdido la materia")
print(nomPerMat)
print(notaPerMat)

print()

nomHabMat = []

notaHabMat = []

#Este bucle permite escoger todos los estudiantes con notas entre 2 y 2.99 y 
#guardarlos en una lista.

for i in range(cantidadEst):
	if promedios[i] >= 2 and promedios[i] < 3:
		nomHabMat.append(nombres[i])
		notaHabMat.append(promedios[i])

print("Estudiantes que deben habilitar")
print(nomHabMat)
print(notaHabMat)

print()

cantiEstAprob = 0

#Este bucle permite contar cuantos estudiantes aprobaron la materia.

for i in range(cantidadEst):
	if promedios[i] >= 3:
		cantiEstAprob = cantiEstAprob + 1

print(f"La cantidad de estudiantes que aprobaron es de {cantiEstAprob}")