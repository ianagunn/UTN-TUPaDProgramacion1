# titulos = ['Las cosas que perdimos en el fuego', 'El principito', 'El retrato de Dorian Gray', 'Las mil y una noches', 'Romeo y Julieta']
# ejemplares = [5, 2, 7, 5, 1]
titulos = []
ejemplares = []
menu = ['1 - Ingresar títulos',
        '2 - Ingresar ejemplares', 
        '3 - Mostrar catálogo', 
        '4 - Consultar disponibilidad', 
        '5 - Listar agotados',
        '6 - Agregar título',
        '7 - Actualizar ejemplares (préstamo/devolución)',
        '8 - Salir']

while True:
    print('====== MENU ======')
    for i in menu:
        print(i)
    opcion = input('Seleccione una opción: ')
    print()

    match opcion:
        case '1':
            print('===== Ingresar títulos =====')
            titulo = input('Ingrese un nuevo título: ')

            while titulo in titulos or titulo == '':
                print('Título ingresado existente o inválido')
                titulo = input('Ingrese el título nuevamente: ')

            titulos.append(titulo)
            # agrega el ejemplar en la misma posicion que el titulo para evitar conflictos utilizando index
            posicion = titulos.index(titulo)
            ejemplares.insert(posicion, 0)
            print(f'Se agregó el nuevo título "{titulo}", con un stock de 0 ejemplares')
        case '2':
            print('===== Ingresar ejemplares =====')

            if not titulos:
                print('No hay titulos en la lista para ingresar ejemplares')
                continue

            ejemplar = int(input('Ingrese la cantidad de ejemplares: '))

            while ejemplar < 0:
                print('El número ingresado es inválido, debe ingresar un número mayor a 0')
                ejemplar = input('Ingrese la cantidad de ejemplares: ')
            
            for i, titulo in enumerate(titulos):
                print(f'{i} - {titulo}')

            posicion = titulos.index(titulo)
            ejemplares.insert(posicion, ejemplar)
            print(f'Se actualizó la cantidad de ejemplares a {ejemplar} en el titulo "{titulo}"')
        case '3':
            print('===== Mostrar catálogo =====')
            for i in range(len(titulos)):
                print('Título: ', titulos[i], '- Ejemplares: ', ejemplares[i])
        case '4':
            print('===== Consultar disponibilidad =====')
            consulta = input('Ingrese título del libro:')
            if consulta in titulos:
                print('apaa')
            else:
                print('Titulo no encontrado')
        case '5':
            print('===== Listar agotados =====')
        case '6':
            print('===== Agregar título =====')
        case '7':
            print('===== Actualizar ejemplares (préstamo/devolución) =====')
        case '8':
            print('Saliendo del programa..')
            break