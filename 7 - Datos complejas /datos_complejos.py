#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#Ejercicio 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

lista = list(precios_frutas.keys())

print(lista)

#Ejercicio 4
agenda = {}

for i in range(5):
    nombre = str(input('\n Ingrese el nombre que desea agendar: '))
    numero = int(input('\n Ingrese el número telefónico: '))
    agenda[nombre] = numero

print('\n ---- Consulta el numero telefónico -----')
buscar = input('\nIngrese el nombre a buscar: ')

if buscar in agenda:
    print(f'El número de {buscar} es {agenda[buscar]}')
else:
    print(f'\n {buscar} no existe en la lista')

#Ejercicio 5
frase = input("Ingrese una frase: ")

palabras = frase.split() 

palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("\nCantidad de veces que aparece cada palabra:")
print(frecuencia)

#Ejercicio 6
alumnos = {}

for i in range(3):
    print("\n----- Alumno -----")
    nombre = input("\nIngrese el nombre del alumno: ")

    print("\n----- Notas -----")
    notas = []
    for j in range(3):
        nota = float(input(f"\nIngrese la nota de {nombre}: "))
        notas.append(nota)
    
    alumnos[nombre] = tuple(notas) 

print("\n----- Promedios -----")
for nombre in alumnos:
    notas_alumno = alumnos[nombre]
    total = 0
    for nota in notas_alumno:
        total += nota
    promedio = total / len(notas_alumno)
    print(f'\n{nombre}: {promedio}')

#Ejercicio 7
parcial_1 = {"Ana", "Juan", "Pedro", "Lucía", "Carla"}
parcial_2 = {"Pedro", "Carla", "María", "Sofía", "Juan"}

print(f'\nLos que aprobaron ambos parciales son {parcial_1&parcial_2}')
print(f'\nLos que aprobaron un solo parcial son {parcial_1^parcial_2}')
print(f'\nLos que aprobaron al menos un parcial son {parcial_1|parcial_2}')

#Ejercicio 8
productos = {'Clavos':100, 'Tornillos': 50, 'Tuercas': 35}
menu = [
    '1 - Consultar stock',
    '2 - Agregar unidades a un producto existente',
    '3 - Agregar un nuevo producto',
    '4 - Salir'
]
while True:
    print('\n----- Menu -----')
    for i in menu:
        print(i)

    opcion = input('Ingrese la opción que desea realizar: ')

    match opcion:
        case '1':
            print('\n----- Consultar stock -----')
            consulta = input('\nIngrese el nombre del articulo que desea consultar stock: ')
            if consulta in productos:
                print(f'\nEl stock de {consulta} es: {productos[consulta]}')
            else:
                print('El producto ingresado no existe')

        case '2':
            print('\n----- Agregar unidades -----')
            consulta = input('\nIngrese el nombre del producto que desea agregar stock: ')
            if consulta in productos:
                agregar = int(input(f'\nIngrese la cantidad que desea agregar para {consulta}: '))
                productos[consulta] += agregar
                print(f'\nEl stock de {consulta} es {productos[consulta]}')

        case '3':
            print('\n----- Agregar nuevo producto -----')
            consulta = input('\nIngrese el nombre del nuevo producto: ')
            if not consulta in productos:
                agregar = int(input(f'\nIngrese el stock para {consulta}: '))
                productos[consulta] = agregar
                print(f'\nSe agregó el nuevo producto {consulta} con un stock de {productos[consulta]}')
            else:
                print('\nEl producto ingresado ya existe')
        case '4':
            print('\nSaliendo..')
            break

#Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "14:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input('Ingrese el día que desea consultar la actividad: ').lower()
hora = input('Ingrese la hora (HH:MM): ')

clave = (dia, hora)
if clave in agenda:
    print(f'El día {dia} a la hora {hora} tenes: {agenda[clave]}')
else:
    print('No hay actividad a esa hora')

#Ejercicio 10
paises = {
    'Argentina':'Buenos Aires',
    'Chile':'Santiago'
}
capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print(capitales)