

n = int(input("Ingrese la cantidad de términos: "))

for i in range(1, n+1):
	sumaDiv = 0
	for j in range(1, i):
		mod = i%j
		if mod == 0:
			sumaDiv = sumaDiv + j
	if sumaDiv == i:
		print(i)