#Suma impar
def impar ():
    print('A continuacion te mostrare la suma total de los numeros impares del 1 al 100')
    suma = 0
    contador = 1
    for i in range(100+1):
        if i % 2 != 0:
            suma = suma + i
            contador += 1
    print(f"La suma total es: {suma}")
            
            
impar()
