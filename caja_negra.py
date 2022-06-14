"""
Pruebas de Caja Negra -> Especificación de función. Se utiliza cuando hay una entrada y salida 
sin conocer el proceso como se realizó.
Unit Test o integration test -> Se prueba función por función . Todos los módulos o funciones conectadas entre si.

"""
import unittest

def suma(num_1, num_2):
        return abs(num_1) + num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado=suma(num_1, num_2)

        self.assertEqual(resultado,15)

    def test_suma_dos_negativos(self):
        num_1 = - 10
        num_2 = -7
        resultado=suma(num_1, num_2)

        self.assertEqual(resultado,-17)

if __name__ == '__main__':
    unittest.main()