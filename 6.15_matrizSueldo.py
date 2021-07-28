#se crea la matriz

matriz = []

#se rellena la matriz con los datos

for f in range(10):
	matriz.append([])
	print()
	print(f"Para el empleado {f+1}: ")
	print()
	for c in range(12):
		if c == 0:
			sueldo = float(input("Ingrese el sueldo de enero: "))
			matriz[f].append(sueldo)
		elif c == 1:
			sueldo = float(input("Ingrese el sueldo de febrero: "))
			matriz[f].append(sueldo)
		elif c == 2:
			sueldo = float(input("Ingrese el sueldo de marzo: "))
			matriz[f].append(sueldo)
		elif c == 3:
			sueldo = float(input("Ingrese el sueldo de abril: "))
			matriz[f].append(sueldo)
		elif c == 4:
			sueldo = float(input("Ingrese el sueldo de mayo: "))
			matriz[f].append(sueldo)
		elif c == 5:
			sueldo = float(input("Ingrese el sueldo de junio: "))
			matriz[f].append(sueldo)
		elif c == 6:
			sueldo = float(input("Ingrese el sueldo de julio: "))
			matriz[f].append(sueldo)
		elif c == 7:
			sueldo = float(input("Ingrese el sueldo de agosto: "))
			matriz[f].append(sueldo)
		elif c == 8:
			sueldo = float(input("Ingrese el sueldo de septiembre: "))
			matriz[f].append(sueldo)
		elif c == 9:
			sueldo = float(input("Ingrese el sueldo de octubre: "))
			matriz[f].append(sueldo)
		elif c == 10:
			sueldo = float(input("Ingrese el sueldo de novienbre: "))
			matriz[f].append(sueldo)
		elif c == 11:
			sueldo = float(input("Ingrese el sueldo de diciembre: "))
			matriz[f].append(sueldo)
	


#matriz = [[1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12], [1,2,3,4,5,6,7,8,9,10,11,12]]

#se imprime la matriz

for f in matriz:
	print(f)

#se guarda la sumatoria del sueldo de cada empleado

for f in range(0, 1):
	totalEmp1 = 0
	for c in range(12):
		totalEmp1 = totalEmp1 + matriz[f][c]
	

for f in range(1, 2):
	totalEmp2 = 0
	for c in range(12):
		totalEmp2 = totalEmp2 + matriz[f][c]
	

for f in range(2, 3):
	totalEmp3 = 0
	for c in range(12):
		totalEmp3 = totalEmp3 + matriz[f][c]
	

for f in range(3, 4):
	totalEmp4 = 0
	for c in range(12):
		totalEmp4 = totalEmp4 + matriz[f][c]


for f in range(4, 5):
	totalEmp5 = 0
	for c in range(12):
		totalEmp5 = totalEmp5 + matriz[f][c]


for f in range(5, 6):
	totalEmp6 = 0
	for c in range(12):
		totalEmp6 = totalEmp6 + matriz[f][c]


for f in range(6, 7):
	totalEmp7 = 0
	for c in range(12):
		totalEmp7 = totalEmp7 + matriz[f][c]


for f in range(7, 8):
	totalEmp8 = 0
	for c in range(12):
		totalEmp8 = totalEmp8 + matriz[f][c]


for f in range(8, 9):
	totalEmp9 = 0
	for c in range(12):
		totalEmp9 = totalEmp9 + matriz[f][c]


for f in range(9, 10):
	totalEmp10 = 0
	for c in range(12):
		totalEmp10 = totalEmp10 + matriz[f][c]





#print(totalEmp1, totalEmp2, totalEmp3, totalEmp4, totalEmp5, totalEmp6, totalEmp7, totalEmp8, totalEmp9, totalEmp10)

#Se guarda el total consignado por mes a los empleados

enero = 0
for f in range(10):
	for c in range(0, 1):
		enero = enero + matriz[f][c]

febrero = 0
for f in range(10):
	for c in range(1, 2):
		febrero = febrero + matriz[f][c]

marzo = 0
for f in range(10):
	for c in range(2, 3):
		marzo = marzo + matriz[f][c]

abril = 0
for f in range(10):
	for c in range(3, 4):
		abril = abril + matriz[f][c]

mayo = 0
for f in range(10):
	for c in range(4, 5):
		mayo = mayo + matriz[f][c]

junio = 0
for f in range(10):
	for c in range(5, 6):
		junio = junio + matriz[f][c]

julio = 0
for f in range(10):
	for c in range(6, 7):
		julio = julio + matriz[f][c]

agosto = 0
for f in range(10):
	for c in range(7, 8):
		agosto = agosto + matriz[f][c]

septiembre = 0
for f in range(10):
	for c in range(8, 9):
		septiembre = septiembre + matriz[f][c]

octubre = 0
for f in range(10):
	for c in range(9, 10):
		octubre = octubre + matriz[f][c]

noviembre = 0
for f in range(10):
	for c in range(10, 11):
		noviembre = noviembre + matriz[f][c]

diciembre = 0
for f in range(10):
	for c in range(11, 12):
		diciembre = diciembre + matriz[f][c]

#print(enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre)

print()
opcion = input("¿Desea conocer el valor de la nómina en función del mes?: ").upper()
print()

if opcion == "SI":
	mes = input("Digite el mes: ").lower()
	print()

	if mes == "enero":
		print(f"El total de la nómina para el mes de {mes} es {enero}")

	if mes == "febrero":
		print(f"El total de la nómina para el mes de {mes} es {febrero}")

	if mes == "marzo":
		print(f"El total de la nómina para el mes de {mes} es {marzo}")

	if mes == "abril":
		print(f"El total de la nómina para el mes de {mes} es {abril}")

	if mes == "mayo":
		print(f"El total de la nómina para el mes de {mes} es {mayo}")

	if mes == "junio":
		print(f"El total de la nómina para el mes de {mes} es {junio}")

	if mes == "julio":
		print(f"El total de la nómina para el mes de {mes} es {julio}")

	if mes == "agosto":
		print(f"El total de la nómina para el mes de {mes} es {agosto}")

	if mes == "septiembre":
		print(f"El total de la nómina para el mes de {mes} es {septiembre}")

	if mes == "octubre":
		print(f"El total de la nómina para el mes de {mes} es {octubre}")

	if mes == "noviembre":
		print(f"El total de la nómina para el mes de {mes} es {noviembre}")

	if mes == "diciembre":
		print(f"El total de la nómina para el mes de {mes} es {diciembre}")

if opcion == "NO":
	pass

print()
opcion2 = input("¿Desea conocer el valor pagado en el año en función del empleado?: ").upper()
print()
	
if opcion2 == "SI":
	empleado = input("Digite el empleado: ")
	print()

	if empleado == "totalEmp1":
		print(f"El total pagado a {empleado} es de {totalEmp1}")

	if empleado == "totalEmp2":
		print(f"El total pagado a {empleado} es de {totalEmp2}")

	if empleado == "totalEmp3":
		print(f"El total pagado a {empleado} es de {totalEmp3}")

	if empleado == "totalEmp4":
		print(f"El total pagado a {empleado} es de {totalEmp4}")

	if empleado == "totalEmp5":
		print(f"El total pagado a {empleado} es de {totalEmp5}")

	if empleado == "totalEmp6":
		print(f"El total pagado a {empleado} es de {totalEmp6}")

	if empleado == "totalEmp7":
		print(f"El total pagado a {empleado} es de {totalEmp7}")

	if empleado == "totalEmp8":
		print(f"El total pagado a {empleado} es de {totalEmp8}")

	if empleado == "totalEmp9":
		print(f"El total pagado a {empleado} es de {totalEmp9}")

	if empleado == "totalEmp10":
		print(f"El total pagado a {empleado} es de {totalEmp10}")

if opcion2 == "NO":
	pass