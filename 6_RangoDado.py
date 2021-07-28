def rangoDado():
    a = float(input("Por favor, ingrese el valor mínimo del rango: "))
    b = float(input("Por favor, ingrese el valor máximo del rango: "))
    c = float(input("Por favor, ingrese un número: "))
    
    if c >= a and c <= b:
        print(f"El número {c} se encuentra dentro del rango")
    else:
        print(f"El número {c} se encuentra fuera del rango")
        
rangoDado()