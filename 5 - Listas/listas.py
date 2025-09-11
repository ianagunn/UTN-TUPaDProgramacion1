#Ejercicio 1
notas_alumnos = [10, 8, 5, 4, 3, 5, 6, 7, 9, 10]
cantidad_notas=10
promedio = 0
suma=0
max = 0
min = 0

print('Lista completa: ', notas_alumnos)

for i in range(cantidad_notas):
    suma = suma+notas_alumnos[i]
promedio = suma/cantidad_notas
print('El promedio de las notas es: ', promedio)

for j in range(cantidad_notas):
    if(notas_alumnos[j] > max):
        max = notas_alumnos[j]
        if(notas_alumnos[j] > 0):
            min = max = notas_alumnos[j]
    if(notas_alumnos[j] < min):
        min = notas_alumnos[j]

print('La nota más alta es:', max)    
print('La nota más baja es:', min)

#Ejercicio 2
lista = []
max_stock = 5

for i in range(max_stock):
    item = str(input('Ingrese un producto: '))
    lista.append(item)

lista.sort()
print('Su lista consta de: ', lista)
eliminar = input('Ingrese el nombre del producto que desea eliminar: ')
if eliminar in lista:
    lista.remove(eliminar)
    print('Su lista ahora consta de: ', lista)
else:
    print('El producto ingresado no existe')

#Ejercicio 3
import random
lista = []
lista_pares = []
lista_impares = []
max_lista = 15

for i in range(max_lista):
    num = random.randint(1, 100)
    lista.append(num)
    if (num % 2) == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print('Lista de todos los números: ', lista)
print('Lista de pares: ', lista_pares, ' y tiene una longitud de: ', len(lista_pares))
print('Lista de impares: ', lista_impares, ' y tiene una longitud de: ', len(lista_impares))

#Ejercicio 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetir = []

longitud = len(datos)

for i in range(longitud):
    if datos[i] not in datos_sin_repetir:
        datos_sin_repetir.append(datos[i])

print(datos_sin_repetir)

#Ejercicio 5
alumnos = ['Valentina', 'Juan', 'Pedro', 'Lucía', 'Raúl', 'Felipe', 'María', 'Kevin']

opcion = int(input('Ingrese 1 si desea agregar un nuevo alumno o 2 si desea eliminar: '))
print()

match opcion:
    case 1:
        #agregar
        print('Lista de alumnos: ', alumnos)
        print()
        alumno = str(input('Ingrese el alumno que quiere agregar: '))
        print()
        alumnos.append(alumno)
    case 2:
        #eliminar
        print('Lista de alumnos: ', alumnos)
        print()
        alumno = str(input('Ingrese el alumno que quiere eliminar: '))
        print()
        if alumno in alumnos:
            alumnos.remove(alumno)
    case _:
        print('Opción inválida, intente nuevamente')

print('La lista de alumnos quedo de la siguiente manera: ', alumnos)

#Ejercicio 6
lista = [1, 2, 3, 4, 5, 6, 7]
longitud = len(lista)

for i in range((longitud-1), 0, -1):
    lista[i], lista[i-1] = lista[i-1], lista[i]

print(lista)

#Ejercicio 7
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

#Ejercicio 8
notas =[
    [10, 6, 7], #estudiante 1
    [8, 8, 7],  #estudiante 2
    [6, 7, 9],  #estudiante 3
    [6, 6, 7],  #estudiante 4
    [4, 4, 5]   #estudiante 5
]
promedio_alumnos = []

for i in range(len(notas)):
    suma=0
    for j in range(len(notas[0])):
        suma += notas[i][j]
    promedio = suma/(len(notas[0]))
    print('El promedio del alumno', i+1,'es =', promedio)

for k in range(len(notas[0])):
    suma=0
    for l in range(len(notas)):
        suma += notas[l][k]
    promedio = suma/(len(notas))
    print('El promedio de la materia', k+1, 'es', promedio )

#Ejercicio 9
tateti =[
    ['-', '-', '-'],
    ['-', '-', '-'], 
    ['-', '-', '-'] 
]

print('Empecemos a jugar TaTeTi!:')

for i in tateti:
    print(i)

for i in range(9):
        jugada = '-'
        x = 0
        y = 0
        x = int(input('El jugador debe ingresar la coordenada X: '))
        y = int(input('El jugador debe ingresar la coordenada Y: '))

        while(jugada != 'X') and (jugada != 'O'):
             jugada = str(input('Ingrese X o O para marcar su jugada: '))

        if tateti[y][x] == '-':
            tateti[y][x] = jugada
        else:
             print('Ese casillero ya está ocupado, perdiste el turno')
        for i in tateti:
            print(i)

#Ejercicio 10

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

