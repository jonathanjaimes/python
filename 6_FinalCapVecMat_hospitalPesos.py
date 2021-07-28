cantidadPacientes = int(input("Ingrese la cantidad de pacientes: "))

nombres = []

pesos = []

objetivos = []

#Este bucle permite crear tantas listas como pacientes haya, además, por cada paciente permite
#introducir su nombre, objetivo y los tres pesos correspondientes.

for f in range(cantidadPacientes):
	pesos.append([])
	print()
	nombre = input(f"Ingrese el nombre del paciente {f+1}: ")
	objetivo = input("Ingrese su objetivo: ganar/perder: ").upper()
	objetivos.append(objetivo)
	nombres.append(nombre)
	for c in range(3):
		peso = float(input(f"Ingrese el peso {c+1} del paciente {f+1}: "))
		pesos[f].append(peso)

print(nombres)

for i in pesos:
	print(i)

print(objetivos)

nomGanPes = []

ganPes = []

nomPerPes = []

perPes = []

#Este bucle permite añadir a una lista los pacientes que ganaron peso.

for f in range(cantidadPacientes):
	if pesos[f][0] < pesos[f][2]:
		diferencia = pesos[f][2] - pesos[f][0]
		ganPes.append(diferencia)
		nomGanPes.append(nombres[f])

print()
print("Los pacientes que ganaron peso son: ")
print(nomGanPes)
print(ganPes)

#Este bucle permite añadir a una lista los pacientes que perdieron peso.

for f in range(cantidadPacientes):
	if pesos[f][0] > pesos[f][2]:
		diferencia = pesos[f][0] - pesos[f][2]
		perPes.append(diferencia)
		nomPerPes.append(nombres[f])

print()
print("Los pacientes que perdieron peso son: ")
print(nomPerPes)
print(perPes)

sumaPerPes = 0

#Este bucle permite sumar todos los pacientes que perdieron peso entre la 1ra y 2da pesada.

for f in range(cantidadPacientes):
	if pesos[f][0] > pesos[f][1]:
		sumaPerPes = sumaPerPes + 1
		
print()
print(f"La cantidad de pacientes que perdieron peso entre la 1ra y 2da pesada es de {sumaPerPes}")

sumaGanar = 0
sumaPerder = 0
sumaIgual = 0

#Este bucle permite contar cuantos pacientes cumplieron objetivo de ganar peso y cuantos cumplieron
#objetivo de perder peso. También cuenta cuantos pacientes mantuvieron el mismo peso.

for f in range(cantidadPacientes):
	if pesos[f][0] < pesos[f][2] and objetivos[f] == "GANAR":
		sumaGanar = sumaGanar + 1
	elif pesos[f][0] > pesos[f][2] and objetivos[f] == "PERDER":
		sumaPerder = sumaPerder + 1
	else:
		sumaIgual = sumaIgual + 1

print()
print(f"La cantidad de pacientes que cumplieron su objetivo fue de {sumaGanar + sumaPerder}")
print(f"La cantidad de pacientes cuyo peso fue el mismo al terminar es de {sumaIgual}")