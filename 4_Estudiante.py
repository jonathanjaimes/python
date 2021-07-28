def notasEstudiante():
    nota1 = float(input("Ingrese el valor de la primera nota: "))
    nota2 = float(input("Ingrese el valor de la segunda nota: "))
    nota3 = float(input("Ingrese el valor de la tercera nota: "))
    nota4 = float(input("Ingrese el valor de la cuarta nota: "))
    nota5 = float(input("Ingrese el valor de la quinta nota: "))
    
    notaDefinitiva = (nota1 + nota2 + nota3 + nota4 + nota5)/5
    
    if notaDefinitiva < 0 or notaDefinitiva > 5:
        print("Nota fuera de rango")
        
    else:
        
    
        if notaDefinitiva >= 3.5:
            print("El estudiante ganó el curso")
            
        else:
            print("El estudiante perdió el curso")
        
notasEstudiante()