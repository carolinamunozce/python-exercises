"""
Leer información de un archivo csv delimitado por comas(,)

"""

import pandas as pd

data = pd.read_csv('./archivos/social_network.csv')
print (data)