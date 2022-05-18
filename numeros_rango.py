"""
Hacer un programa que muestre todos los números entre dos números (rango) que diga el usuario

"""

numero1=int(input('Ingrese el primer número del rango: '))
numero2=int(input('Ingrese el segundo numero del rango: '))

if numero1<numero2:
    for i in range(numero1, (numero2+1)):
        print(i)
else:
    print("No se puede crear el rango")