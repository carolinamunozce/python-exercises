# "Ejemplo 1"
# def tabla(numero):
#     print(f'La tabla de multuplicar del numero: {numero}')

#     for i in range(11):
#         operacion = numero * i
#         print (f'{numero} x {i} = {operacion}')

# tabla(5)

# print('___________________________')
# for numero_tabla in range(1,11):
#     tabla(numero_tabla)

# "Ejemplo2"

# def getEmpleado(nombre, dni='False'):
#     print(f'nombre: {nombre}')
    
#     if dni!=False:
#         print(f'dni {dni}')

# getEmpleado('Carolina', '1234')

# # Ejemplo parametros opcionales y return

# def saludame(nombre):
#     saludos =f'Hola, saluods {nombre}'
#     return saludos
# saludame("Caro")


#Ejemplo Calculadora

def calculadora(numero1, numero2, basicas=False):
    print(numero1,numero2)
    suma = (numero1 + numero2)
    resta = numero1 - numero2   
    multiplicación = numero1 * numero2
    division=numero1 / numero2

    cadena =""
    if basicas!=False:
        cadena +="Suma:"+str(suma)
        cadena +="\n"
        cadena +="Resta:"+str(resta)
        cadena +="\n"
    else:
        cadena +="Multiplicacion:"+str(multiplicación)
        cadena +="\n"
        cadena +="Division:"+str(division)
        cadena +="\n"
    
    return cadena

print(calculadora(5, 3, False))

#Ejemplo, Función dentro de otra

def getNombre(nombre):
    texto = (f'El nombre es : {nombre}')
    return texto
def getApellidos(Apellidos):
    texto = (f'El nombre es : {Apellidos}')
    return texto
def devuelveTodo(nombre, Apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(Apellidos)
    return texto
print(devuelveTodo("carolina","muñoz"))