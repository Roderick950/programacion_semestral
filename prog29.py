def prog29():     
    print("Calcular la tarifa de un taxi")

    distancia = float(input("Ingresa la distancia recorrida en km: "))

    dist_inicial = 10

     
    if distancia <= dist_inicial: 
        tarifa_inicial = 2.50
        tarifa_total = distancia * tarifa_inicial
        print(f'La tarifa total es $ {tarifa_total}')
         
    else: 
        distancia > dist_inicial
        tarifa_inicial = 2.50
        tarifa_ad = 2.00
        tarifa_total2 = dist_inicial * tarifa_inicial +  (distancia - dist_inicial) * 2.00
        print(f'La tarifa adicional es ${tarifa_total2: .2f}')
        
       
