import pandas as pd
fbk = ['Facebook', 2449, True]
twt = ['Twitter',339 , False]
ig = ['Instagram',1000, True]
yt = ['Youtube',2000, False]
lkn = ['Linkedin' , 663, False]
wsp = ['Whatsapp',1600, True]

nombres_rrss = ['Facebook','Twitter','Instagram','Youtube','Linkedin','Whatsapp']

print(nombres_rrss[1], nombres_rrss[2], nombres_rrss[3])
print(nombres_rrss[2:5])
print(nombres_rrss[-1])

#Agregar las
fbk.append(2006)
print(fbk)

twt.append(2006)
ig.append(2010)
yt.append(2005)
lkn.append(2003)
wsp.append(2009)

fbk.remove(2006)
print(fbk)

lista_rrss = [fbk, twt, ig,yt, lkn, wsp]

# Se deben agregar las columnas del dataframe
data = pd.DataFrame(lista_rrss, columns=['Nombre', 'Cantidad','es_fbk','Año'])
print(data)