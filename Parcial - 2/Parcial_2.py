productos = {}
menu = [
    '1 - Ingresar títulos (múltiples)',
    '2 - Ingresar ejemplares',
    '3 - Mostrar catálogo',
    '4 - Consultar disponibilidad',
    '5 - Listar agotados',
    '6 - Agregar título',
    '7 - Actualizar ejemplares (préstamo/devolución)',
    '8 - Salir\n'
]
while True:
    print('----- Menu -----\n')
    for i in menu:
        print(i)
    
    opcion = input('Ingrese la opción que desea ejecutar: ')

    match opcion:
        case '1':
            print('----- Ingresar títulos (múltiples) -----\n')
            while True:
                #Se pide ingresar el título y cantidad, validando que este ingresado correctamente.
                titulo = str(input('Escriba el título que desea ingresar: '))
                while (titulo in productos) and (titulo == ''):
                    titulo = str(input('El título ingresado está vacío o ya existe. Escriba nuevamente: '))
                cantidad = int(input(f'Ingrese el stock para {titulo}: '))
                while cantidad <= 0:
                    print('La cantidad ingresada debe ser mayor a 0\n')
                    cantidad = int(input(f'Ingrese el stock nuevamente para {titulo}: '))

                #Una vez validados los input, se guarda en el csv
                with open('inventario.csv', 'a') as archivo:
                    archivo.write(f'{titulo}, {cantidad}\n')

                print(f'\nSe agregó el nuevo título {titulo} con un stock de {cantidad}\n')

                #Se pregunta si se quiere seguir agregando titulos
                seguir = input('Desea continuar agregando títulos? Ingresa S para Si y N para No: ').lower()
                if seguir == 'n':
                    break
                while seguir != 's' and seguir != 'n':
                    seguir = input('Opción incorrecta, ingresa S para Si y N para No: ').lower()
                    if seguir == 'n':
                        break
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case '8':
            break