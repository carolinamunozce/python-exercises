"""
Escribir un programa que muestre los cuadrados(numero multiplicado por si mismo), 
de los primeros 60 números naturales

Resolverlo con for y con while

"""
# For
print("********************** Ciclo For**********************************")
for i in range(1,61):
    print(f'El cuadrado de {i} es : {i**2}')

print("**********************Ciclo While*********************************")
#While
i=0
while i <=60:
    print(f'El cuadrado de {i} es : {i**2}')
    i+=1