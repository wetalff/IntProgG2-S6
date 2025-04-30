#numeros pares
def NumPares(limite):
    print(f"Numeros pares hasta {limite}: ")
    for contador in range(0, limite +1):
        if contador % 2 == 0:
            print(contador)
def main():
    limite = int(input("Ingrese el numero limite para contar los pares antes de el: "))
    NumPares(limite)
    
    
main()


       
        
     
   