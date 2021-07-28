#En esta función se ingresan los datos

def tomaDatos():
  a = float(input("Ingrese el valor de a: "))
  b = float(input("Ingrese el valor de b: "))
  c = float(input("Ingrese el valor de c: "))
  return a, b, c

a, b, c = tomaDatos()

#En esta función se toman los datos ingresados y se ejecuta la operación.

def discriminante(a, b, c):
  dis = (b**2) - 4*a*c
  return dis

dis = discriminante(a, b, c)

#En esta función se ejecuta el segundo procedimiento

def procedimiento(a, b, dis):
  x1 = (-b + (dis)**(1/2))/2*a
  x2 = (-b - (dis)**(1/2))/2*a
  return x1, x2

#Esta condición permite ejecutar la tercera función solo si el valor de retorno de la segunda función cumple la condición especificada.

if dis >= 0 and a != 0:
  x1, x2 = procedimiento(a, b, dis)
  print(f"La solución a la ecuación es {x1} y {x2}")
else:
  print("La ecuación no tiene solución")