# titulos = ['las cosas que perdimos en el fuego', 'el principito', 'el retrato de dorian gray', 'las mil y una noches', 'romeo y julieta']
# ejemplares = [1, 5, 3, 0, 15]
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
            if len(titulos) != 0:
                print('Ya tenes titulos cargados. Para añadir nuevos titulos, utiliza la opción 6 - Agregar título')
                print()
                continue

            while True:
                titulo = input('Ingrese un nuevo título: ').lower()
                print()

                while titulo == '' or titulo in titulos:
                    print('Título ingresado existente o vacío')
                    titulo = input('Ingrese un nuevo título: ').lower()
                    print()

                ejemplar = input(f'Ingrese la cantidad de ejemplares para {titulo}: ')
                print()

                while not ejemplar.isdigit() or int(ejemplar) < 0:
                    print('Debe ingresar un número entero mayor o igual a 0')
                    print()
                    ejemplar = input('Ingrese la cantidad de ejemplares para {titulo}: ')   
                    print()

                titulos.append(titulo)
                posicion = titulos.index(titulo)
                ejemplar = int(ejemplar)
                ejemplares.insert(posicion, ejemplar)
                print(f'Se agregó el nuevo título "{titulo}", con un stock de {ejemplar} ejemplares')
                print()

                seguir = input('¿Desea agregar más titulos? Marque S para seguir o N para no seguir: ').lower()
                print()
                
                while seguir != 's' and seguir != 'n':
                    print('Opción ingresada incorrecta')
                    print()
                    seguir = input('¿Desea agregar más titulos? Marque S para seguir o N para no seguir: ').lower()
                    print()

                if seguir == 'n':
                    break

        case '2':
            print('===== Ingresar ejemplares =====')
            print()

            if not titulos:
                print('No hay titulos en la lista para ingresar ejemplares')
                print()
                continue
            
            ejemplar = input('Ingrese la cantidad de ejemplares: ')
            print()
            ejemplar = int(ejemplar)

            while ejemplar < 0:
                print('El número ingresado es inválido, debe ingresar un número mayor a 0')
                print()
                ejemplar = input('Ingrese la cantidad de ejemplares: ')
                print()
            ejemplar = int(ejemplar)
            
            for i, titulo in enumerate(titulos):
                print(f'{i} - {titulo}')

            print()    
            posicion = input('Ingrese el número del titular al que desea ingresar ejemplares: ')
            print()
            
            while posicion > len(ejemplares) or posicion < 0:
                print('El número ingresado no existe')
                print()
                posicion = input('Ingrese el número del titular al que desea ingresar ejemplares: ')
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

            if len(titulos) == 0:
                print('No tenes titulos cargados. Para cargar titulos debes ingresar la opción 1 - Ingresar títulos')
                print()
                continue

            while True:
                titulo = input('Ingrese un nuevo título: ').lower()
                print()

                while titulo == '' or titulo in titulos:
                    print('Título ingresado existente o vacío')
                    titulo = input('Ingrese un nuevo título: ').lower()
                    print()

                ejemplar = input(f'Ingrese la cantidad de ejemplares para "{titulo}": ')
                print()

                while not ejemplar.isdigit() or int(ejemplar) < 0:
                    print('Debe ingresar un número entero mayor o igual a 0')
                    print()
                    ejemplar = input(f'Ingrese la cantidad de ejemplares para "{titulo}": ')   
                    print()

                titulos.append(titulo)
                posicion = titulos.index(titulo)
                ejemplar = int(ejemplar)
                ejemplares.insert(posicion, ejemplar)
                print(f'Se agregó el nuevo título "{titulo}", con un stock de {ejemplar} ejemplares')
                print()

                seguir = input('¿Desea agregar más titulos? Marque S para seguir o N para no seguir: ').lower()
                print()
                
                while seguir != 's' and seguir != 'n':
                    print('Opción ingresada incorrecta')
                    print()
                    seguir = input('¿Desea agregar más titulos? Marque S para seguir o N para no seguir: ').lower()
                    print()

                if seguir == 'n':
                    break

        case '7':
            print('===== Actualizar ejemplares (préstamo/devolución) =====')
            print()

            if len(titulos) == 0:
                print('No tenes títulos cargados. Primero debes ingresar títulos en la opción 1 - Ingresar títulos')
                print()
                continue

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
                        print(f'"{titulos[posicion]}" no tiene stock suficiente para realizar un prestamo')
                        print()
                        continue
                    
                    ejemplares[posicion] -= 1
                    print(f'Se realizó el prestamo de "{titulos[posicion]}" satisfactoriamente')
                    print()

                case '2':
                    print('===== Devolución =====')
                    print()

                    ejemplares[posicion] += 1
                    print(f'Se realizó la devolución de "{titulos[posicion]}" satisfactoriamente')
                    print()
        case '8':
            print('Saliendo del programa..')
            print()
            break