grupos = int(input("Ingrese la cantidad de grupos: "))

grupos = grupos + 65
sumaPeriodoGrupos = 0
sumaExcluidos = 0
sumaCondicionales = 0
sumaEstudiantesPeriodoPerdido = 0
sumaCantEst = 0
for i in range(65, grupos):
	print()
	print(f"Grupo {chr(i)}")
	print()
	cantidadEstudiantes = int(input(f"Ingrese la cantidad de estudiantes del grupo {chr(i)}: "))
	cantidadEstudiantes = cantidadEstudiantes + 1
	sumaNotasEstudiantes = 0
	cantidadExcluido = 0
	cantidadCondicional = 0
	estudiantesPeriodoPerdido = 0
	cantEst = 0
	for j in range(1, cantidadEstudiantes):
		print()
		print(f"Estudiante {j}")
		print()
		sumNotas = 0
		cantidadMateriasPerdidas = 0
		cantEst = cantEst + 1
		
		for materia in range(1, 7):
			print(f"Materia {materia}")
			print()
			nota = float(input(f"Ingrese la nota de la materia {materia}: "))
			print()
			if nota < 3:
				cantidadMateriasPerdidas = cantidadMateriasPerdidas + 1
			sumNotas = sumNotas + nota
		promedioPeriodoEstudiante = sumNotas / 6
		if promedioPeriodoEstudiante < 2:
			cantidadExcluido = cantidadExcluido + 1
		
		if promedioPeriodoEstudiante < 2 or cantidadMateriasPerdidas > 3:
			estado = "Excluido"
		if promedioPeriodoEstudiante >= 2 and promedioPeriodoEstudiante <= 2.9 and cantidadMateriasPerdidas <= 3:
			cantidadCondicional = cantidadCondicional + 1
			estado = "Condicional"
		if promedioPeriodoEstudiante < 3:
			estudiantesPeriodoPerdido = estudiantesPeriodoPerdido + 1
		if promedioPeriodoEstudiante >= 3:
			estado = "Normal"

		print(f"El promedio del periodo para el estudiante {j} es {promedioPeriodoEstudiante} y su estado es {estado}")

		sumaNotasEstudiantes = sumaNotasEstudiantes + promedioPeriodoEstudiante
	sumaCantEst = sumaCantEst + cantEst
	promedioPeriodoGrupo = sumaNotasEstudiantes / j
	print()
	print(f"El promedio del grupo {chr(i)} es: {promedioPeriodoGrupo}")
	sumaPeriodoGrupos = sumaPeriodoGrupos + promedioPeriodoGrupo
	print()
	#print(f"La cantidad de estudiantes excluidos en el grupo {chr(i)} es de {cantidadExcluido}")
	#print(f"La cantidad de estudiantes condicionales en el grupo {chr(i)} es de {cantidadCondicional}")
	print(f"La cantidad de estudiantes que reprobaron en el grupo {chr(i)} es de {estudiantesPeriodoPerdido}")
	print(f"La cantidad de estudiantes que aprobaron en el grupo {chr(i)} es de {cantidadEstudiantes - estudiantesPeriodoPerdido}")
	sumaExcluidos = sumaExcluidos + cantidadExcluido
	sumaCondicionales = sumaCondicionales + cantidadCondicional
	sumaEstudiantesPeriodoPerdido = sumaEstudiantesPeriodoPerdido + estudiantesPeriodoPerdido
promedioTodosGrupos = sumaPeriodoGrupos / (grupos-65)
print()
print(f"El promedio de todos los grupos es de: {promedioTodosGrupos}")
print(f"La cantidad total de excluidos por todos los grupos es de {sumaExcluidos} y su porcentaje es {(sumaExcluidos*100)/sumaCantEst}%")
print(f"La cantidad total de condicionales por todos los grupos es de {sumaCondicionales}")
print(f"La cantidad total de estudiantes reprobados por todos los grupos es de {sumaEstudiantesPeriodoPerdido}")
print(f"La cantidad total de estudiantes aprobados por todos los grupos es de {sumaCantEst - sumaEstudiantesPeriodoPerdido} y su porcentaje es {((sumaCantEst - sumaEstudiantesPeriodoPerdido)*100)/sumaCantEst}%")
print(sumaCantEst)