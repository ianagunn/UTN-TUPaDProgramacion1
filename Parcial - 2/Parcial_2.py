import os
import csv

#Se define la variable para el archivo inventario.csv
nombre_archivo = "inventario.csv"

#Muestra el menu principal del programa
def menu():
    menu = [
        "1 - Ingresar títulos (múltiples)",
        "2 - Ingresar ejemplares",
        "3 - Mostrar catálogo",
        "4 - Consultar disponibilidad",
        "5 - Listar agotados",
        "6 - Agregar título",
        "7 - Actualizar ejemplares (préstamo/devolución)",
        "8 - Salir\n"
    ]

    while True:
        print("-"*40)
        for i in menu:
            print(i)
        print("-"*40)
        
        opcion = input("Ingrese la opción que desea ejecutar: ").strip()

        match opcion:
            case "1":
                ingresar_titulos()
            case "2":
                ingresar_ejemplares()
            case "3":
                mostrar_catalogo()
            case "4":
                consultar_disponibilidad()
            case "5":
                listar_agotados()
            case "6":
                agregar_titulo()
            case "7":
                actualizar_ejemplares()
            case "8":
                print("Cerrando programa...\n")
                break
            case _:
                print("La opción seleccionada no existe.\n")

#Si el archivo inventario.csv no existe, lo crea poniendo el header TITULO y CANTIDAD
def crear_archivo():
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['TITULO', "CANTIDAD"])
            escritor.writeheader()

        print(f"Se ha creado el archivo {nombre_archivo}\n")

#Se encarga de ir a buscar la información del catalogo
def obtener_catalogo():
    catalogo = []
    if not os.path.exists(nombre_archivo):
        return catalogo
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            catalogo.append({
                "TITULO": fila["TITULO"],
                "CANTIDAD": int(fila["CANTIDAD"])
            })

    return(catalogo)

#Muestra el listado de titulares con su respectiva cantidad. La información la trae utilizando la función obtener_catalogo()
def mostrar_catalogo():
    print("\n----------- Mostrar catalogo -----------")
    catalogo = obtener_catalogo()
    if not catalogo:
        print("El catálogo está vacío.\n")
        return

    print("TITULO  -  CANTIDAD")
    
    for producto in catalogo:
        print(f'{producto["TITULO"]}  -  {producto["CANTIDAD"]}')

#Busca si un titulo existe en un catalogo. La información la trae utilizando la función obtener_catalogo()
def existe_titulo(titulo):
    catalogo = obtener_catalogo()

    for producto in catalogo:
        if titulo.strip().lower() == producto["TITULO"].strip().lower():
            return True
        
    return False

#Se encarga de agregar titulos al catalogo
def agregar_titulos(producto):
    with open(nombre_archivo, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
        escritor.writerow(producto)

#Le pide al usuario cuantos titulos desea agregar, pide los datos y los guarda en inventario.csv
def ingresar_titulos():
    print("\n----------- Ingresar titulos -----------")

    titulares = input("Ingrese la cantidad de titulares que desea agregar: ")
    if not titulares.isdigit():
        print("\nDebe ingresar un número entero\n")
        return
    while int(titulares) < 0:
        titulares = input("Ingrese una cantidad de titulares mayor a 0: ")

    titulares = int(titulares)

    for i in range(titulares):
        while True:
            titulo = input("\nIngrese el titulo del libro: ").strip()
            if titulo == "":
                print("El titulo ingresado no puede estar vacío")
                continue

            if existe_titulo(titulo):
                print("\nEl titulo ya existe en el catálogo")
                continue

            cantidad = input("\nIngrese la cantidad de ejemplares: ")
            while not cantidad.isdigit():
                cantidad = input("\nIngrese una cantidad en número entero mayor a 0: ")
            while int(cantidad) < 0:
                cantidad = input("\nIngrese una cantidad de ejemplares mayor a 0: ")
            cantidad = int(cantidad)

            agregar_titulos({"TITULO": titulo, "CANTIDAD": cantidad})

            print(f"\nSe agregó el titulo {titulo} correctamente")
            break

#Actualiza el catalogo con la cantidad de ejemplares para un titulo
def guardar_ejemplares(catalogo):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
        escritor.writeheader()
        escritor.writerows(catalogo)

#Pide al usuario ingresar un titulo y luego debe ingresar la cantidad de ejemplares que necesita agregar
def ingresar_ejemplares():
    print("\n----------- Ingresar ejemplares -----------")

    titulo = input("\nIngrese el nombre del titular que desea agregar ejemplares: ").strip()
    if not titulo:
        print("El titulo ingresado está vacío")
        return
    
    catalogo = obtener_catalogo()
    encontrado = False
    for producto in catalogo:
        if producto["TITULO"].lower() == titulo.lower():
            encontrado = True

            cantidad = input("\nIngrese la cantidad de ejemplares que desea agregar: ")
            while not cantidad.isdigit():
                cantidad = input("\nIngrese una cantidad en número entero mayor a 0: ")
            while int(cantidad) < 0:
                cantidad = input("\nIngrese una cantidad de ejemplares mayor a 0: ")

            cantidad = int(cantidad)
            producto["CANTIDAD"] += cantidad
            guardar_ejemplares(catalogo)
            print("\nLos ejemplares fueron añadidos con éxito\n")
            break
    if not encontrado:
        print("\nEl titulo ingresado no existe\n")

#Muestra la disponibilidad de ejemplares que tiene un titulo
def consultar_disponibilidad():
    print("\n----------- Consultar disponibilidad -----------")
    catalogo = obtener_catalogo()
    consulta = input("Ingrese el titulo que desea consultar disponibilidad: ").strip()
    encontrado = False
    for producto in catalogo:
            if producto["TITULO"].strip().lower() == consulta.lower():
                print(f"\n{producto["TITULO"]} tiene {producto["CANTIDAD"]} ejemplares disponibles\n")
                encontrado = True
                break
    
    if not encontrado:
        print("\nEl titulo ingresado no existe\n")

#Muestra una lista de titulos que se encuentran agotados
def listar_agotados():
    print("\n----------- Listar agotados -----------")
    catalogo = obtener_catalogo()
    encontrado = False
    for producto in catalogo:
        if int(producto["CANTIDAD"]) == 0:
            encontrado = True
            print(f"\n{producto["TITULO"]}\n")
    if not encontrado:
        print("\nNo hay titulares agotados\n")

#Agrega un titulo individualmente con su cantidad de ejemplares
def agregar_titulo():
    print("\n----------- Agregar titulo -----------")
    while True:
        titulo = input("\nIngrese el titulo del libro: ").strip()
        if titulo == "":
            print("El titulo ingresado no puede estar vacío ")
            continue

        if existe_titulo(titulo):
            print("El titulo ya existe")
            continue

        cantidad = input("\nIngrese la cantidad de ejemplares: ")
        while not cantidad.isdigit():
            cantidad = input("\nIngrese una cantidad en número entero mayor a 0: ")
        while int(cantidad) < 0:
            cantidad = input("\nIngrese una cantidad de ejemplares mayor a 0: ")
        cantidad = int(cantidad)

        agregar_titulos({"TITULO": titulo, "CANTIDAD": cantidad})

        print("\nSe agregó el titulo correctamente")
        return

#Pide un titulo y si existe, el usuario debe ingresar como lo quiere actualizar dependiendo si es Prestamo o devolución. 
#Para prestamo resta 1 y para devolución suma 1 en los ejemplares del titulo
def actualizar_ejemplares():
    print("\n----------- Actualizar ejemplares -----------")
    titulo = input("\nIngrese el nombre del titulo que desea actualizar: ").strip()

    if not titulo:
        print("El titulo ingresado está vacío")
        return
    
    catalogo = obtener_catalogo()
    encontrado = False
    for producto in catalogo:
        if producto["TITULO"].lower() == titulo.lower():
            encontrado = True
            print("1 - Prestamo")
            print("2 - Devolución")
            opcion = input("Ingrese la opcion: ")

            if not opcion.isdigit():
                print("\nOpción incorrecta, debes ingresar 1 o 2\n")
                return
            
            if int(opcion) == 1:
                if producto["CANTIDAD"] > 0:
                    producto["CANTIDAD"] -= 1
                    guardar_ejemplares(catalogo)
                    print("\nSe actualizo el ejemplar con el prestamo\n")
                    break
                else:
                    print("No hay ejemplares disponibles para este titular\n")
            elif int(opcion) == 2:
                producto["CANTIDAD"] += 1
                guardar_ejemplares(catalogo)
                print("\nSe actualizo el ejemplar con la devolución\n")
                break
            else:
                print("\nOpción inválida\n")

    if not encontrado:
        print("\nNo se encuentra el titulo en el catalogo\n")

#LLama a crear el archivo csv si hace falta
crear_archivo()

#Llama al menu para interactuar con las funciones
menu()