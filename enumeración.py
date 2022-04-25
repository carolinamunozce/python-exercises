#Determinar si un número tiene una raiz cuadrada exactamente
objetivo = int(input("Escoge un objetivo : "))
respuesta = 0

while respuesta **2 < objetivo:
    print (respuesta)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene raíz cuadrada exacta')
