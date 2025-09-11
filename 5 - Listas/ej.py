reporte_ventas =[
    [1, 3, 5, 2],
    [7, 20, 18, 21],
    [8, 21, 10, 13],
    [30, 50, 26, 33],
    [1, 0, 6, 9],
    [4, 4, 7, 3],
    [60, 40, 30, 20]
]
max = 0

for i in range(len(reporte_ventas)):
    suma = 0
    for j in range(len(reporte_ventas[0])):
        suma += reporte_ventas[i][j]
    print(f'El día {i+1} vendió un total de: ', suma)
print()

for k in range(len(reporte_ventas[0])):
    suma = 0
    for l in range(len(reporte_ventas)):
        suma += reporte_ventas[l][k]
    if suma > max:
        max = suma
        producto = k+1

    print(f'El producto {k+1} vendió un total de: ', suma)
print()
print('El producto que más vendió', producto)
