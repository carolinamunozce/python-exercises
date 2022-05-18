"""
Crear una variable llamada "Pais" y "Continente"
Mostrar por pantalla e imprimir ambas
Poner un comentario diciendo que tipo es
"""

pais = input("Ingrese un país : ")
continente = input("Ingrese un continente : ")
print(f'El pais es: {pais} y el continente es: {continente}')
tipo_pais=type(pais)
print(f'El país tiene tipo: {type(pais)}  y el continente tiene tipo + {type(continente)}')
