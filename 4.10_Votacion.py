contAndroid = 0
contiOS = 0

while True:
	respuesta = input("Cual plataforma prefiere, Android o iOS?: ")
	respuesta = respuesta.lower()
	#print(respuesta)

	if respuesta == "android":
		contAndroid = contAndroid + 1

	elif respuesta == "ios":
		contiOS = contiOS + 1

	else:
		print("Opción inválida")

	if respuesta == "android" or respuesta == "ios":
		salir = input("Desea ver el resultado de la votación? (si o no): ")
		if salir == "si":
			break

print(f"Los votos contados para la plataforma Android son: {contAndroid}")
print(f"Los votos contados para la plataforma iOS son: {contiOS}")