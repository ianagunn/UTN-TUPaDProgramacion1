temperaturas =[
    [12, 20], #día 1
    [8, 18],  #día 2
    [15, 23], #día 3
    [14, 20], #día 4
    [8, 15],  #día 5
    [15, 22], #día 6
    [19, 25]  #día 7
]
suma_min = 0
suma_max = 0
cant_filas = len(temperaturas)
cant_columnas = len(temperaturas[0])

for i in range(cant_filas):
    for j in range(cant_columnas):
        if j == 0:
            suma_min += temperaturas[i][j]
        else:
            suma_max += temperaturas[i][j]

promedio_min = suma_min/cant_filas
promedio_max = suma_max/cant_filas

print('El promedio de máximas estuvo en ', promedio_max, ', mientras que el de mínimas estuvo en', promedio_min)