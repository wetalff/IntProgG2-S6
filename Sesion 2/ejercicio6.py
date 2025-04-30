#Promedio de calificaciones
def promedio():
    suma = 0
    contador = 0
    for _ in range(1000):
      calificacion = float(input("Ingrese la calificacion: "))
      if calificacion == -1:
          break
      suma += calificacion
      contador += 1
    if contador > 0:
         prom = suma / contador
         print("El promedio es: ", prom)
    else:
        print("No se ingresaron calificaciones") 
        
promedio()
              
   