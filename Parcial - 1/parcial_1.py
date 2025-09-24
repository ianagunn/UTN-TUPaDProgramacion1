titulos = ['las cosas que perdimos en el fuego', 'el principito', 'el retrato de dorian gray', 'las mil y una noches', 'romeo y julieta']
ejemplares = [1, 5, 3, 0, 15]
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
    print()
    for i in menu:
        print(i)
    print()
    opcion = input('Seleccione una opción: ')
    print()

    match opcion:
        case '1':
            print('===== Ingresar títulos =====')
            print()
            titulo = input('Ingrese un nuevo título: ').lower()
            print()

            while titulo in titulos or titulo == '':
                print('Título ingresado existente o inválido')
                print()
                titulo = input('Ingrese el título nuevamente: ')
                print()

            titulos.append(titulo)
            # agrega el ejemplar en la misma posicion que el titulo para evitar conflictos utilizando index
            posicion = titulos.index(titulo)
            ejemplares.insert(posicion, 0)
            print(f'Se agregó el nuevo título "{titulo}", con un stock de 0 ejemplares')
            print()
        case '2':
            print('===== Ingresar ejemplares =====')
            print()

            if not titulos:
                print('No hay titulos en la lista para ingresar ejemplares')
                print()
                continue
            
            ejemplar = input('Ingrese la cantidad de ejemplares: ')
            print()

            while ejemplar < 0:
                print('El número ingresado es inválido, debe ingresar un número mayor a 0')
                print()
                ejemplar = input('Ingrese la cantidad de ejemplares: ')
                print()
            ejemplar = int(ejemplar)
            
            for i, titulo in enumerate(titulos):
                print(f'{i} - {titulo}')

            print()    
            posicion = input('Ingrese el número del titular al que desea cambiar la cantidad de ejemplares: ')
            print()
            
            while posicion > len(ejemplares) or posicion < 0:
                print('El número ingresado no existe')
                print()
                posicion = input('Ingrese el número del titular al que desea cambiar la cantidad de ejemplares: ')
                print()

            posicion = int(posicion)
            ejemplares[posicion] += ejemplar
            print(f'Se agregaron {ejemplar} ejemplares al título "{titulos[posicion]}"')
            print()
        case '3':
            print('===== Mostrar catálogo =====')
            print()

            for i in range(len(titulos)):
                print('Título: ', titulos[i], '- Ejemplares: ', ejemplares[i])
            print()
        case '4':
            print('===== Consultar disponibilidad =====')
            print()
            consulta = input('Ingrese título del libro: ').lower()
            print()

            if consulta in titulos:
                posicion = titulos.index(consulta)
                print(f'El ejemplar {consulta} tiene una disponibilidad de {ejemplares[posicion]}')
                print()
            else:
                print('Titulo no encontrado')
                print()
        case '5':
            print('===== Listar agotados =====')

            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f'{titulos[i]} - Agotado')
        case '6':
            print('===== Agregar título =====')
            print()
            titulo = input('Ingrese el nuevo título: ').lower()
            print()

            while titulo in titulos or titulo == '':
                print('Título ingresado existente o inválido')
                print()
                titulo = input('Ingrese el título nuevamente: ').lower()
                print()
            
            ejemplar = input(f'Ingrese la cantidad de ejemplares: ')
            print()
            while not ejemplar.isdigit() or int(ejemplar) < 0:
                print('Debe ingresar un número entero mayor o igual a 0')
                print()
                ejemplar = input(f'Ingrese la cantidad de ejemplares nuevamente: ')   
                print()

            titulos.append(titulo)
            # agrega el ejemplar en la misma posicion que el titulo para evitar conflictos utilizando index
            posicion = titulos.index(titulo)
            ejemplar = int(ejemplar)
            ejemplares.insert(posicion, ejemplar)
            print(f'Se agregó el nuevo título "{titulo}", con un stock de {ejemplar} ejemplares')
            print()
        case '7':
            print('===== Actualizar ejemplares (préstamo/devolución) =====')
            print()
            titulo = input('Ingrese titulo que desea actualizar ejemplares: ').lower()
            print()
        
            while titulo not in titulos or titulo == '':
                print('Título ingresado no existente o inválido')
                print()
                titulo = input('Ingrese el título nuevamente: ').lower()
                print()

            posicion = titulos.index(titulo)

            for i in accion:
                print(i)

            print()
            actualizar = input(f'Ingresa el indice de la acción que desea realizar: ')
            print()

            match actualizar:
                case '1':
                    print('===== Prestamo =====')
                    print()
                    if ejemplares[posicion] == 0:
                        print(f'{titulos[posicion]} no tiene stock')
                        print()
                        continue
                    cantidad = input(f'Ingrese la cantidad que desea prestar para el titulo "{titulo}": ')
                    print()

                    while not cantidad.isdigit() or int(cantidad) <= 0:
                        print('La cantidad ingresada debe ser mayor a 0')
                        print()
                        cantidad = input(f'Ingrese nuevamente la cantidad que desea prestar para el titulo "{titulo}": ')
                        print()

                    if int(cantidad) > int(ejemplares[posicion]):
                        print(f'{titulos[posicion]} no tiene stock suficiente')
                        continue
                    ejemplares[posicion] -= int(cantidad)

                case '2':
                    print('===== Devolución =====')
                    print()
                    cantidad = input(f'Ingrese la cantidad que están devolviendo para el titulo "{titulo}": ')
                    print()
                    ejemplares[posicion] += int(cantidad)
        case '8':
            print('Saliendo del programa..')
            print()
            break