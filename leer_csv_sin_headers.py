"""
Leer información de un archivo csv sin headers

"""

import pandas as pd

data = pd.read_csv('./archivos/social_network_sin_headers.csv', header=None, names=["Nombre","Cantidad","Es_FBK","Anio"])
print (data)