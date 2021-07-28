"""
for i in range(90, 64, -1):
	print(chr(i))


lista = []

for i in range(90, 64, -1):
	
	car = chr(i)
	lista.append(car)
	print(lista)

"""
contador = 90

for i in range(90, 64, -1):
	contador = contador - 1
	for h in range(90, contador, -1):
		print(chr(h),end=" ")
	print()