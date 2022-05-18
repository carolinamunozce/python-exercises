"""
Programa que pide las notas de 15 alumnos y tiene que decir cuantos reprueban y cuantos pasan
"""
aprobado=0
reprobado=0
no_validas=0

cantidad_alumnos =  int(input('Ingrese la cantidad de alumnos a ingresar notas:'))
for i in range(0,cantidad_alumnos):
    notas = int(input(f'Ingrese nota alumno: {i+1}:'))
    if notas >=40 and notas<=70:
        aprobado+=1
    elif notas < 40:
        reprobado+=1
    else:
        no_validas+=1
print(f'Los alumnos aprobados son:' + str(aprobado))
print(f'Los alumnos reprobados son:' + str(reprobado))
print(f'Los alumnos con notas no válidas son:' + str(no_validas))

