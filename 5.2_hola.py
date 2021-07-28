def nombre():
	nombre1 = input("Ingrese el primer nombre: ")
	nombre2 = input("Ingrese el segundo nombre: ")
	return nombre1, nombre2




def printt(a, b):
	print(f"Hola {a}")
	print(f"Hola {b}")

nom1, nom2 = nombre()
printt(nom1, nom2)