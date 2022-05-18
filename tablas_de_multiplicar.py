"""
Mostrar todas las tablas de multiplicar, del 1 al 10.
Mostrando el titulo de la tabla y las multiplicaciones del 1 al 10

"""

print("******** Tablas de Multiplicar ********")
for i in range(1,11):
    print("###########################################")
    print(f"########## Tabla del {i} ###################")
    print("###########################################")
    numero=1
    while numero <= 10:
        print(f'El resultado de la multiplicación de {i} * {numero} es =  {numero*i}')
        numero+=1
    print('\n') #Salto de línea