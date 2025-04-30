#Suma de números hasta alcanzar un límite

def suma():
 suma = 0
 for _ in range (1000):
  num = int(input("Ingrese el numero: "))
  suma = suma + num
  if suma > 100:
    break
 print("La suma total es: ", suma)

suma()
        
    

    
    
    
    
    

  