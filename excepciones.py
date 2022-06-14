"""
Manejo de excepciones -> 
Se relacionan a errores de semántica.
No silenciar las excepciones(solo imprimir por consola)
Se ocupa el Try, except y finally. 
Para ocupar las propias excepciones ocupar Raise
Divide los elementos de la lista por un divisors"""
def divide_elementos_de_la_lista(lista, divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_la_lista(lista,divisor))