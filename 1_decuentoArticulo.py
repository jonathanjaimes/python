def descuentoArticulo():
    
    x = 0
    
    while x == 0:
    
        valorArticulo = float(input("Por favor, ingrese el valor del artículo: "))
        descuento = 0.05
        
        if valorArticulo > 150000:
            nuevoValor = valorArticulo - (valorArticulo*descuento)
        
        else:
            nuevoValor = valorArticulo
    
        print(f"El valor de su artículo es {nuevoValor}")



descuentoArticulo()