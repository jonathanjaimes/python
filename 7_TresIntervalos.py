def tresIntervalor():
    
    a = float(input("Por favor, ingrese el valor mínimo del primer intervalo: "))
    b = float(input("Por favor, ingrese el valor máximo del primer intervalo: "))
    
    c = float(input("Por favor, ingrese el valor mínimo del segundo intervalo: "))
    d = float(input("Por favor, ingrese el valor máximo del segundo intervalo: "))
    
    e = float(input("Por favor, ingrese el valor mínimo del tercer intervalo: "))
    f = float(input("Por favor, ingrese el valor máximo del tercer intervalo: "))
    
    x = float(input("Por favor, ingrese un número: "))
    
    while a >= b or b >= c or c >= d or d >= e or e >= f:
        print("Rango invalido, vuelva a intentarlo")
        
        a = float(input("Por favor, ingrese el valor mínimo del primer intervalo: "))
        b = float(input("Por favor, ingrese el valor máximo del primer intervalo: "))
        
        c = float(input("Por favor, ingrese el valor mínimo del segundo intervalo: "))
        d = float(input("Por favor, ingrese el valor máximo del segundo intervalo: "))
        
        e = float(input("Por favor, ingrese el valor mínimo del tercer intervalo: "))
        f = float(input("Por favor, ingrese el valor máximo del tercer intervalo: "))
        
        x = float(input("Por favor, ingrese un número: "))
    
    if x >= a and x <= b:
        print(f"El número {x} se encuentra dentro del primer intervalo")
    elif x >= c and x <= d:
        print(f"El número {x} se encuentra dentro del segundo intervalo")
    elif x >= e and x <= f:
        print(f"El número {x} se encuentra dentro del tercer intervalo")
    else:
        print(f"El número {x} no se encuentra dentro de ninguno de los tres intervalos")
        
tresIntervalor()