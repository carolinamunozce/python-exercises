"""
Prueba de Caja de Cristal-> Se basan en el flujo del programa.
Prueba todos los caminos prosibles de una función. Ramificaciones, bucles for y while, recursión.
Se utiliza para Regression testing o mockup
Se asume que ya hay código escrito98n .
"""
import unittest

def es_mayor_de_edad(edad):
    if edad >=18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad=20
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)
    
    def test_es_menor_de_edad(self):
        edad=16
        resultado=es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)
if __name__ == '__main__':
    unittest.main()