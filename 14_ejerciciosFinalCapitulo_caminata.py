mayor = 0
menor = 9999

for mes in range(1, 5):
	print(f"Mes {mes}")
	sumaPromSemana = 0
	sumaDiasMes = 0
	for semana in range(1, 5):
		print(f"Semana {semana}")
		sumaDias = 0
		diasCaminataTrue = 0
		
		for dia in range(1, 8):

			tiempoDia = int(input(f"Ingrese el tiempo de caminata en minutos para el día {dia}: "))
			if tiempoDia > mayor:
				mayor = tiempoDia
			if tiempoDia < menor and tiempoDia != 0:
				menor = tiempoDia
			if tiempoDia != 0:
				sumaDias = sumaDias + tiempoDia
				diasCaminataTrue = diasCaminataTrue + 1
				sumaPromSemana = sumaPromSemana + tiempoDia
				sumaDiasMes = sumaDiasMes + 1
			#sumaDiasMes = sumaDiasMes + tiempoDia
		promedioSemana = sumaDias/diasCaminataTrue
		print(f"El promedio de tiempo de la semana {semana} fue de: {promedioSemana}")
		

	promedioMes = sumaPromSemana/sumaDiasMes
	print(f"El promedio de tiempo del mes {mes} fue de {promedioMes}")

print(f"El mayor tiempo fue: {mayor}")
print(f"El menor tiempo fue: {menor}")