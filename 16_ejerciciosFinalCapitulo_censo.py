
contadorPrimaria = 0
contadorSecundaria = 0
contadorProfesional = 0
contadorMaestria = 0
contadorDoctorado = 0
contadorPersonas = 0
contadorHombres = 0
contadorMujeres = 0
contadorHombresPrimaria = 0
contadorTitulo = 0
contadorMujeresPos = 0
contadorAntioquia = 0
contadorCundinamarca = 0
contadorSantander = 0
while True:

	while True:
		nivelEstudio = input('''Ingrese su nivel de estudios:
p: Primaria
s: Secundaria
pf: Profesional
m: Maestria
d: Doctorado
''')
		nivelEstudio = nivelEstudio.upper()
		if nivelEstudio == "P" or nivelEstudio == "S" or nivelEstudio == "PF" or nivelEstudio == "M" or nivelEstudio == "D":
			break

	while True:
		genero = input("Ingresar el género h/f: ")
		genero = genero.upper()
		if genero == "H" or genero == "F":
			break

	

	

	contadorPersonas = contadorPersonas + 1

	if nivelEstudio == "P":
		contadorPrimaria = contadorPrimaria + 1

	elif nivelEstudio == "S":
		contadorSecundaria = contadorSecundaria + 1

	elif nivelEstudio == "PF":
		contadorProfesional = contadorProfesional + 1

	elif nivelEstudio == "M":
		contadorMaestria = contadorMaestria + 1

	elif nivelEstudio == "D":
		contadorDoctorado = contadorDoctorado + 1

	if genero == "H":
		contadorHombres = contadorHombres + 1

	elif genero == "F":
		contadorMujeres = contadorMujeres + 1

	if genero == "H" and nivelEstudio == "P":
		contadorHombresPrimaria = contadorHombresPrimaria + 1


	while True:
		edadTituloProfesional = int(input("Ingrese la edad a la que se graduó: "))
		
		if edadTituloProfesional > 10 and edadTituloProfesional < 150:
			break

	if edadTituloProfesional < 25 and nivelEstudio == "PF":
		contadorTitulo = contadorTitulo + 1

	if genero == "F" and (nivelEstudio == "M" or nivelEstudio == "D"):
		contadorMujeresPos = contadorMujeresPos + 1

	while True:
		departamento = input("Ingrese el departamento: ")

		departamento = departamento.upper()

		if departamento == "ANTIOQUIA" or departamento == "CUNDINAMARCA" or departamento == "SANTANDER":
			break

	if departamento == "ANTIOQUIA":
		contadorAntioquia = contadorAntioquia + 1

	if departamento == "CUNDINAMARCA":
		contadorCundinamarca = contadorCundinamarca + 1

	if departamento == "SANTANDER":
		contadorSantander = contadorSantander + 1

	continuar = input("Desea continuar si/no: ")
	continuar = continuar.upper()
	if continuar == "NO":
		break

porcentajePrimaria = (contadorPrimaria / contadorPersonas) * 100
porcentajeSecundaria = (contadorSecundaria / contadorPersonas) * 100
porcentajeProfesional = (contadorProfesional / contadorPersonas) * 100
porcentajeMaestria = (contadorMaestria / contadorPersonas) * 100
porcentajeDoctorado = (contadorDoctorado / contadorPersonas) * 100

if contadorMujeres == 0:
	porcentajeMujeresPos = 0
else:
	porcentajeMujeresPos = (contadorMujeresPos / contadorMujeres) * 100

print(f"El porcentaje total de personas que tienen estudios de primaria es de {porcentajePrimaria}%")
print(f"El porcentaje total de personas que tienen estudios de secundaria es de {porcentajeSecundaria}%")
print(f"El porcentaje total de personas que tienen estudios de profesional es de {porcentajeProfesional}%")
print(f"El porcentaje total de personas que tienen estudios de maestria es de {porcentajeMaestria}%")
print(f"El porcentaje total de personas que tienen estudios de doctorado es de {porcentajeDoctorado}%")
print(f"El porcentaje total de mujeres con posgrado es de {porcentajeMujeresPos}%")
print(f"Cantidad de hombres con estudios de solo primaria {contadorHombresPrimaria}")
print(f"Cantidad de hombres y mujeres que hayan recibido su titulo profesional antes de cumplir 25 años de edad es de {contadorTitulo}")

if contadorAntioquia != 0 and genero == "H" and nivelEstudio == "P":
	print(f"Cantidad de hombres con solo estudio de primaria en Antioquia es de {contadorAntioquia}")

if contadorCundinamarca != 0 and genero == "H" and nivelEstudio == "P":
	print(f"Cantidad de hombres con solo estudio de primaria en Cundinamarca es de {contadorCundinamarca}")

if contadorSantander != 0 and genero == "H" and nivelEstudio == "P":
	print(f"Cantidad de hombres con solo estudio de primaria en Santander es de {contadorSantander}")