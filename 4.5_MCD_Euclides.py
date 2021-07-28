a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número distinto: "))

copiaA = a
copiaB = b

c= copiaA % copiaB

while c != 0:
    copiaA = copiaB
    copiaB = c
    c= copiaA % copiaB




print(f"El Máximo Común Divisor de los numeros {a} y {b} es {copiaB}")

mcm = (a*b)//copiaB

print(f"El Mínimo Común Multiplo de los números {a} y {b} es {mcm}")