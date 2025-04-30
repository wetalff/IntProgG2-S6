#Contador regresivo
def contador (numero):
    for i in range(numero, -1, -1):
        print("Conteo regresivo: ", i)
            
def main ():
    numero = int(input("Ingresa un numero positivo para hacer la cuenta regresiva: "))
    contador(numero)

main()
