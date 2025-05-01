#Serie de fibonacci

def fibonacci():
    a = 0
    b = 1
    n = int(input("Ingrese un numero para marcar el limite de la serie de fibonacci: "))
    for i in range(n):
        print (a)
        next = a + b
        a = b
        b = next
        
        
fibonacci ()


