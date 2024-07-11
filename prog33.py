def prog33():       
    print("suma dígitos de un número \n")

    n= int(input("Introduce un número entero: "))

    suma_digitos = 0
    n = abs(n)  

    while n > 0:
        digito = n % 10  
        suma_digitos += digito  
        n = n// 10  

    print("La suma de los dígitos es->", suma_digitos)

