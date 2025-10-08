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
#Ejercicio 7
#Ejercicio 8
#Ejercicio 9
#Ejercicio 10