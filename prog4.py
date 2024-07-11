def prog4():  
    print("calculo de temperatura de celcius a  fahrenheit y kelvin ")
    celcius = float(input("ingrese grados celcius:"))
    kelvin  = float(input("ingrese grados celcius para kelvin:"))
    fahrenheit = (celcius * (9/5 ) )+ 32
    kelvin = (celcius + 273.15)
    print(f" son {fahrenheit} grados fahrenheit ,y son {kelvin} grados kelvin")


