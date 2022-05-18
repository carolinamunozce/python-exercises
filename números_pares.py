"""
Escribir un script que permita mostrar por pantalla todos los números pares del 1 al 120
"""

pares = [i if i % 2 == 0 else 0 for i in range(1,121)  ]
print(f'{pares} es par')