def prog16():
        print('programa que calcula el precio con descuento')
    precio = float(input("Ingrese el precio del producto: "))

    if precio > 100: 
        descuento = precio * 0.1
        p_final = precio - descuento
        print(f'$', p_final)
        print("Se ha realizado un descuento del precio del producto")
        
    else: 
        p_final = precio
        print(f'$', p_final)
        print(f'No se aplica descuento')
        
