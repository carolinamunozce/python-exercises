"""
Hacer un programa que muestre todos los números impares 
entre dos números de decida el usuario

"""

numero1 = int(input('Ingrese el primer número del rango : '))
numero2 = int(input('Ingrese el segundo número del rango : '))
if(numero1 < numero2):
    impares = [i for i in range(numero1, numero2+1) if i % 2 == 1]
    print(impares)
else:
    print('El rango no es válido')