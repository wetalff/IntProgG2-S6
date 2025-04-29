#leer un numero ingresado por el usuario
#Mostrar la letra a por cada numero del 1 al numero
#ingresado por el usuario ejemplo, numero: 3
#a
#aa
#aaa

def mostrarLetras(numero):
    for i in range(numero+1):
        print(f"a"* i)
        
        
def main():
    num = int(input("Ingresa un numero: "))
    mostrarLetras (num)
    
    
main()
    