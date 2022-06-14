"""
Afirmaciones -> Son parte de la programación defensiva.
nos preparamos para saber si las entradas son del tipo que esperamos
Nos aseguramos que el usuario no cometa un error"""


def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es de tipo str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])
    return primeras_letras

lista = ['hola', 'que', 'hace']
palabras = (primera_letra(lista))
print(palabras)
