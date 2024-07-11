def prog1(): 
    #programa que calcula el salario
    print("programa que calcula el salario de un chambeador")
    i = float(input('ingrese las horas trabajadas : '))
    x = float(input('ingrese las horas extras trabajadas : '))
    resultado = (x + i )* 3.00
    print(f"tu salario es de",resultado)
