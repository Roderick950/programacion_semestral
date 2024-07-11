def prog19():         
    print('programa que compara dos numeros')
    num_1 = float(input("Ingresa el primer numero:  "))
    num_2 = float(input("Ingresa el segundo numero: "))

    if num_1 > num_2: 
        num_mayor = num_1
        print("El primer numero es mayor")
        
    elif num_1 == num_2:
        print("Ambos numeros son iguales")
        
    else: 
        num_mayor = num_1
        print("El segundo numero es mayor")
