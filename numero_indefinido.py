"""
Pedir al usuario que ingrese número y que solo termine el programa cuando ingrese el valor 111
"""
i = 0
while i<100:
    numero =int(input("Ingrese un número : "))
    if numero ==111:
        print('El número ingresado es 111. El programa ha finalizado')
        break
    else:
        pass

