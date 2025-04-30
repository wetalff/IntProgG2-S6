#Adivinar
import random
def adivinar():
    numero = random.randint(1, 10)
    print("Adivina el numero secreto")
    for _ in range(100):
     num = int(input("Ingrese un numero del 1 al 10: "))
     if num > numero:
        print("Elige un numero mas bajo")
     elif num < numero:
        print("Elige un numero mas alto")
     else:
        print("Felicidades acertaste!")
        break
        
    
adivinar()


    
    
    

