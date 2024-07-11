def prog21():    
    print('programa que determina si un salario es neto')
    salario = float(input("Ingrese su salario bruto: $ "))

    if salario > 2000:
        impuesto = salario * 0.2
        salario_neto = salario - impuesto
        print(f"El salario neto luego de aplicar el impuesto es ${salario_neto}")

    else:
        salario_neto = salario
        print(f"El salario neto sin cobrar impuestos es ${salario}")
