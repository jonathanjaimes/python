def tomaValores():
	lado = float(input("Ingrese la longitud del lado del hexágono: "))
	return lado

def hallaPerimetro(lado):
	perimetro = lado*6
	return perimetro

def hallaApotema(lado):
	apotema = ((lado**2)-((lado**2)/4))**(1/2)
	return apotema

def areaHex(apotema, perimetro):
	area = (perimetro*apotema)/2
	return area

def salida(area):
	print(f"El área de un hexágono es {area}")


lado = tomaValores()

perimetro = hallaPerimetro(lado)

apotema = hallaApotema(lado)

area = areaHex(apotema, perimetro)

salida(area)