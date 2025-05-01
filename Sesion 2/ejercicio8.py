#Menu
def menu():
   print("Bienvenido al menu interactivo!")
   print("Saludar, 1")
   print("Fecha, 2")
   print("Salir, 3")
   for _ in range(1000):
       opcion = int(input("¿que opción deseas ejecutar?: "))
       if opcion == 1:
           print("¡Hola como estas!")
       elif opcion == 2:
           print("Hoy es 30 de abril del 2025")
       elif opcion == 3:
          print("¡Nos vemos!")
          break
       else:
          print("Elige una opción valida")
        
       
     
           
       
menu()
   








