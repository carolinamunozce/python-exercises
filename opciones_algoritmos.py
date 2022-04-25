# Programa que permite mostrar las diferentes formas de mostrar un raíz cuadrada

# El algoritmo de enumeración exhaustiva permite generar todas las opciones posibles para calcular un valor
def enumeracion(objetivo):
    respuesta = 0
    while respuesta **2 < objetivo:
        print (respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raíz cuadrada exacta')

# El algoritmo de aproximción permite generar el valor aproximado para calcular
def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon **2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta<= objetivo:
        print (abs(respuesta**2 -objetivo),respuesta)
        respuesta +=paso

    if abs(respuesta**2 -objetivo) >= epsilon :
        print(f'No se encoontró la raíz cuadrada del {objetivo}')
    else:
        print(f'La raíz cuadrada de número es {respuesta}')

# Permite dividir el valor para encontrar mas rapidamente el resultado a necesitar
def busqueda_binaria(objetivo):
    epsilon= 0.01
    bajo= 0.0 
    alto = max(1.0, objetivo)
    respuesta=(alto+bajo)/2
    while abs(respuesta**2 -objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto},respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo=respuesta
        else:
            alto=respuesta
    
            respuesta = (alto + bajo)/2
    print(f'La raíz cuadrada del {objetivo} es {respuesta}')

def opciones():

    opcion = int(input('Ingrese una opción para calcular su raíz con las siguientes formas:\n 1) Enumeración, 2) Aproximación y 3) Búsqueda binaria: '))
    if opcion == 1:
        objetivo = int(input("Ingrese un número a calcular:"))
        enumeracion(objetivo)
    elif opcion== 2:
        objetivo = int(input("Ingrese un número a calcular:"))
        aproximacion(objetivo)
    elif opcion== 3:
        objetivo = int(input("Ingrese un número a calcular:"))
        busqueda_binaria(objetivo)
    else:
        print("Opción no válida") 

opciones()