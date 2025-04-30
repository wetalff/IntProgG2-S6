#tabla de multiplicar del 1 al 10
def TablaMult(numero):
    print(f"Tabla de multiplicar del {numero}: ")
    for i in  range(1,11):
        respuesta = numero * i
        print(f"{numero} * {i} = {respuesta}")
   
   
def main():        
    num = int(input("Ingrese el numero para ver su tabla de multiplicar: "))
    TablaMult(num)



main()