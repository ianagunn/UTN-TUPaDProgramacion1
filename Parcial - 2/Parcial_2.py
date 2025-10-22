import os
import csv

nombre_archivo = "inventario.csv"

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
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                print("Cerrando programa...\n")
                break
            case _:
                print("La opción seleccionada no existe.\n")
def crear_archivo():
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['TITULO', "CANTIDAD"])
            escritor.writeheader()

        print(f"Se ha creado el archivo {nombre_archivo}\n")

def obtener_catalogo():
    catalogo = []
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            catalogo.append({
                "TITULO": fila["TITULO"],
                "CANTIDAD": int(fila["CANTIDAD"])
            })
    return(catalogo)

def mostrar_catalogo():
    print("----------- Mostrar catalogo -----------")
    catalogo = obtener_catalogo()
    print("TITULO  CANTIDAD")
    for producto in catalogo:
        print(f"{producto["TITULO"]}  -  {producto["CANTIDAD"]}")

def existe_titulo(titulo):
    catalogo = obtener_catalogo()

    for producto in catalogo:
        if titulo.strip() == producto["TITULO"].lower():
            return True
        
    return False

def agregarTitulo(producto):
    with open(nombre_archivo, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
        escritor.writerow(producto)


def ingresar_titulos():
    print("\n----------- Ingresar titulos -----------")
    while True:
        while True:
            titulo = input("\nIngrese el titulo del libro: ").strip()
            if titulo == "":
                print("El titulo ingresado no puede estar vacío ")
                continue

            if existe_titulo(titulo):
                print("El titulo ya existe")
                seguir = input('\n¿Desea continuar agregando títulos? (si/no): ').strip()
                if seguir.lower() != 'si':
                    continue  
                else:
                    break

            cantidad = int(input("Ingrese la cantidad de ejemplares: "))
            while cantidad < 0:
                cantidad = int(input("Ingrese una cantidad de ejemplares mayor o igual a cero: "))

            agregarTitulo({"TITULO": titulo, "CANTIDAD": cantidad})

            print("\nSe agregó el titulo correctamente")

            seguir = input('\n¿Desea continuar agregando títulos? (si/no): ').strip()
            if seguir.lower() != 'si':
                return  
            else:
                break
def guardarEjemplares(catalogo):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
        escritor.writeheader()
        escritor.writerows(catalogo)

def ingresar_ejemplares():
    print("\n----------- Ingresar ejemplares -----------")

    titulo = input("\nIngrese el nombre del titulo que necesita agregar ejemplares: ").strip()
    if not titulo:
        print("El titulo ingresado está vacío")
        return
    
    catalogo = obtener_catalogo()

    for producto in catalogo:
        if producto["TITULO"].lower() == titulo.lower():
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))

            if cantidad <= 0:
                print("\nLa cantidad es menor o igual a cero")
            else:
                producto["CANTIDAD"] += cantidad
                guardarEjemplares(catalogo)
                print("\nLos ejemplares fueron añadidos con éxito")
                break
        else:
            print("\nNo se encuentra el titulo en el catalogo")

def consultar_disponibilidad():
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

crear_archivo()
menu()