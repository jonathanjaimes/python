import time

while True:
  m = int(input("Ingrese los minutos: "))
  if m < 61:
    break

# contará las horas
for hora in range(0, -1, -1):
  #hora = str(hora)

#contará los minutos  
  for minuto in range(m-1, -1, -1):
    #minuto = str(minuto)

#mientras minuto sea menor a diez, lo va a convertir a cadena y lo va a concatenar con un cero a la izquierda    

    if minuto < 10:
        minuto = "0" + str(minuto)
#contará los segundos
#por cada 59 segundos, el minuto iterará una vez y por cada 59 minutos la hora iterará una vez 
    for segundo in range(59, -1, -1):     
      #segundo = str(segundo)
      #if minuto < 10:
        
        #minuto = str(minuto)
        #minuto = "0" + str(minuto)

#mientras segundo sea menor a diez, lo va a convertir a cadena y lo va a concatenar con un cero a la izquierda          
        if segundo < 10:
        
        #segundo = str(segundo)
            segundo = "0" + str(segundo)
     
        print("0" + str(hora) + ":" + str(minuto) + ":" + str(segundo))
        time.sleep(1)

#El if inferior lanza la alerta cuando se cumpla 00:05:00
        if minuto == "05" and segundo == "00":
          print("Faltan cinco minutos")