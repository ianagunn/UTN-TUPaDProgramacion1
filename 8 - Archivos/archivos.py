#1. Escribe agregando inventario al archivo productos.txt
with open('/Users/ian/Documents/GitHub/UTN-TUPaDProgramacion1/8 - Archivos/productos.txt', 'w') as archivo:
    archivo.write('Nombre, Precio, Cantidad\n')
    archivo.write('Destornillador,15000,10\n')
    archivo.write('Martillo,16000,8\n')
    archivo.write('Taladro,100000,5\n')

#2. Leé el archivo producto.txt
with open('/Users/ian/Documents/GitHub/UTN-TUPaDProgramacion1/8 - Archivos/productos.txt', 'r') as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    linea = linea.strip()
    nombre, precio, cantidad = linea.split(',')
    print(f'Nombre: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')

#3. Agrega productos al archivo producto.txt
with open('/Users/ian/Documents/GitHub/UTN-TUPaDProgramacion1/8 - Archivos/productos.txt', 'a') as archivo:
    nombre = input('Ingrese el nombre del producto que desea agregar: \n')
    precio = input('Ingrese el precio del producto que desea agregar: \n')
    cantidad = input('Ingrese la cantidad del producto que desea agregar: \n')
    archivo.write(f'{nombre}, {precio}, {cantidad}')

#4. Cargar productos en una lsita de diccionario
productos = []

with open('/Users/ian/Documents/GitHub/UTN-TUPaDProgramacion1/8 - Archivos/productos.txt', 'r') as archivo:
    i=0
    for linea in archivo:
        if i != 0:
            producto = linea.strip().split(',')
            nombre = producto[0]
            precio = producto[1]
            cantidad = producto[2]
            productos.append({
                'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad
            })
        else:
            i += 1

#5. Buscar productos por nombre
buscar = input('Ingrese el nombre del producto a buscar: \n')
flag = False
for p in productos:
    if p['nombre'] == buscar:
        print(f'Nombre: {p['nombre']}')
        print(f'Precio {p['precio']}')
        print(f'Cantidad: {p['cantidad']}')
        flag = True

if flag == False:
    print('El producto no existe\n')

#6. Cargar productos en una lista de diccionarios
with open('/Users/ian/Documents/GitHub/UTN-TUPaDProgramacion1/8 - Archivos/productos.txt', 'w') as archivo:
    archivo.write('Nombre, Precio, Cantidad\n')
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")