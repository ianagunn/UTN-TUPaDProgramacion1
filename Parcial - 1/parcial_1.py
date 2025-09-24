titulos = ['Las cosas que perdimos en el fuego', 'El principito', 'El retrato de Dorian Gray', 'Las mil y una noches', 'Romeo y Julieta']
ejemplares = [5, 0, 7, 0, 1]
# titulos = []
# ejemplares = []
menu = ['1 - Ingresar títulos',
        '2 - Ingresar ejemplares', 
        '3 - Mostrar catálogo', 
        '4 - Consultar disponibilidad', 
        '5 - Listar agotados',
        '6 - Agregar título',
        '7 - Actualizar ejemplares (préstamo/devolución)',
        '8 - Salir']

accion = ['1 - Prestamo',
          '2 - Devolución']

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
            
            ejemplar = input('Ingrese la cantidad de ejemplares: ')

            while not ejemplar.isdigit() or int(ejemplar) < 0:
                print('Debe ingresar un número entero mayor o igual a 0')
                ejemplar = input('Ingrese la cantidad de ejemplares: ')
            ejemplar = int(ejemplar)
            
            for i, titulo in enumerate(titulos):
                print(f'{i} - {titulo}')
                
            posicion = int(input('Ingrese a que titular le desea cambiar la cantidad de ejemplares: '))
            ejemplares[posicion] += ejemplar
            print(f'Se agregaron ejemplares a {ejemplar} al titulo "{titulos[posicion]}"')
        case '3':
            print('===== Mostrar catálogo =====')
            for i in range(len(titulos)):
                print('Título: ', titulos[i], '- Ejemplares: ', ejemplares[i])
        case '4':
            print('===== Consultar disponibilidad =====')
            consulta = input('Ingrese título del libro: ')
            if consulta in titulos:
                posicion = titulos.index(consulta)
                print(f'El ejemplar {consulta} tiene una disponibilidad de {ejemplares[posicion]}')
            else:
                print('Titulo no encontrado')
        case '5':
            print('===== Listar agotados =====')
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f'{titulos[i]} - Agotado')
        case '6':
            print('===== Agregar título =====')
            titulo = input('Ingrese el nuevo título: ')

            while titulo in titulos or titulo == '':
                print('Título ingresado existente o inválido')
                titulo = input('Ingrese el título nuevamente: ')
            
            ejemplar = input(f'Ingrese la cantidad de ejemplares: ')

            titulos.append(titulo)
            # agrega el ejemplar en la misma posicion que el titulo para evitar conflictos utilizando index
            posicion = titulos.index(titulo)
            ejemplares.insert(posicion, ejemplar)
            print(f'Se agregó el nuevo título "{titulo}", con un stock de {ejemplar} ejemplares')
        case '7':
            print('===== Actualizar ejemplares (préstamo/devolución) =====')
            titulo = input('Ingrese titulo que desea actualizar ejemplares: ')

            while titulo not in titulos or titulo == '':
                print('Título ingresado no existente o inválido')
                titulo = input('Ingrese el título nuevamente: ')

            posicion = titulos.index(titulo)

            for i in accion:
                print(i)

            actualizar = input(f'Ingresa el indice de la acción que desea realizar: ')

            match actualizar:
                case '1':
                    print('===== Prestamo =====')
                    if ejemplares[posicion] == 0:
                        print(f'{titulos[posicion]} no tiene stock')
                        continue
                    cantidad = input(f'Ingrese la cantidad que desea prestar para el titulo {titulo}: ')

                    while int(cantidad) <= 0:
                        print('La cantidad ingresada debe ser mayor a 0')
                        cantidad = input(f'Ingrese nuevamente la cantidad que desea prestar para el titulo {titulo}: ')

                    if int(cantidad) > int(ejemplares[posicion]):
                        print(f'{titulos[posicion]} no tiene stock suficiente')
                        continue
                    ejemplares[posicion] -= int(cantidad)

                case '2':
                    print('===== Devolución =====')
                    cantidad = input(f'Ingrese la cantidad que estan devooviendo para el titulo {titulo}: ')
                    ejemplares[posicion] += int(cantidad)
        case '8':
            print('Saliendo del programa..')
            break