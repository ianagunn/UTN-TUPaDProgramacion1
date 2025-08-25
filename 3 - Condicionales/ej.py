#Ejercicio 10

mes = input("Ingrese mes: ")
dia = input("Ingrese día: ")
hemisferio = input("Ingrese hemisferio: ")

hemisferio = hemisferio.lower()

#Hemisferio Norte
if hemisferio == "norte":
    #invierno
    if mes == "diciembre" and dia >= 21:
        print("Invierno")
    elif mes == "enero":
        print("Invierno")
    elif mes == "febero":
        print("Invierno")
    elif mes == "marzo" and dia<=20:
        print("Invierno")
    #primavera
    elif mes == "marzo" and dia >= 21:
        print("Primavera")
    elif mes == "abril":
        print("Primavera")
    elif mes == "mayo":
        print("Primavera")
    elif mes == "junio" and dia<=20:
        print("Primavera")
    #Verano
    elif mes == "junio" and dia >= 21:
        print("Verano")
    elif mes == "julio":
        print("Verano")
    elif mes == "agosto":
        print("Verano")
    elif mes == "septiembre" and dia<=20:
        print("Verano")
    #Otoño
    elif mes == "septiembre" and dia >= 21:
        print("Otoño")
    elif mes == "octubre":
        print("Otoño")
    elif mes == "noviembre":
        print("Otoño")
    elif mes == "diciembre" and dia<=20:
        print("Otoño")


#Hemisferio Sur
if hemisferio == "sur":
    #verano
    if mes == "diciembre" and dia >= 21:
        print("Verano")
    elif mes == "enero":
        print("Verano")
    elif mes == "febero":
        print("Verano")
    elif mes == "marzo" and dia<=20:
        print("Verano")
    #otoño
    elif mes == "marzo" and dia >= 21:
        print("Otoño")
    elif mes == "abril":
        print("Otoño")
    elif mes == "mayo":
        print("Otoño")
    elif mes == "junio" and dia<=20:
        print("Otoño")
    #invierno
    elif mes == "junio" and dia >= 21:
        print("Invierno")
    elif mes == "julio":
        print("Invierno")
    elif mes == "agosto":
        print("Invierno")
    elif mes == "septiembre" and dia<=20:
        print("Invierno")
    #primavera
    elif mes == "septiembre" and dia >= 21:
        print("Primavera")
    elif mes == "octubre":
        print("Primavera")
    elif mes == "noviembre":
        print("Primavera")
    elif mes == "diciembre" and dia<=20:
        print("Primavera")