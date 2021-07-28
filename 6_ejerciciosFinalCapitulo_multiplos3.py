while True:

	n = int(input("Ingrese la cantidad de terminos mayor a 6: "))

	if n > 6:
		break


for i in range(6, n+1):
	if i%3 == 0:
		print(i)