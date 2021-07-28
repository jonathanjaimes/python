import math

def areaHex(num):

	def tomaValores():
		lado = float(input(f"Ingrese la longitud del lado del hexágono {num}: "))
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

	return area

areaHex1 = areaHex(1)
areaHex2 = areaHex(2)
areaHex3 = areaHex(3)


def areaCirculo(num):
	radio = float(input(f"Ingrese el radio del círculo {num}: "))
	area = math.pi*radio**2
	return area

areaCriculo1 = areaCirculo(1)
areaCriculo2 = areaCirculo(2)

def areaRectangulo(num):
	ancho = float(input(f"Ingrese el ancho del rectángulo {num}: "))
	alto = float(input(f"Ingrese el alto del rectángulo {num}: "))
	area = ancho * alto
	return area

areaRectangulo1 = areaRectangulo(1)
areaRectangulo2 = areaRectangulo(2)
areaRectangulo3 = areaRectangulo(3)
areaRectangulo4 = areaRectangulo(4)

sumaAreas = areaHex1 + areaHex2 + areaHex3 + areaCriculo1 + areaCriculo2 + areaRectangulo1 + areaRectangulo2 + areaRectangulo3 + areaRectangulo4

print(f"El área total del parque infantil es {sumaAreas} unidades cuadradas")