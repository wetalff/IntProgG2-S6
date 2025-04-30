#Número de dígitos
def conteo():
    conteo_Digitos = 0
    numero = int(input("Ingresa un numero entero positivo para contar sus digitos: "))
    if numero <= 0:
        print("Ingresa un numero entero positivo")
        return
    for _ in range (numero):
     if numero > 0:
        numero = numero// 10
        conteo_Digitos +=1
    
    print("La cantidad total de digitos del numero que me mencionaste es de: ", conteo_Digitos)
    
conteo ()

