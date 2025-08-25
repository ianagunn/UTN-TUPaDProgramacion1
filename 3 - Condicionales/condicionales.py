#Ejercicio 1

edad = int(input("Ingrese su edad: "))
edad_maxima = 18

if edad>edad_maxima:
    print("Es mayor de edad")

#Ejercicio 2

nota = float(input("Ingrese su nota: "))
nota_minima = 6

if nota >= nota_minima:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3

num = int(input("Ingrese número par: "))

if (num%2)==0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad<12:
    print("Niño/a: menor de 12 años.")
elif (edad>=12)and(edad<18):
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif (edad>=18)and(edad<30):
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif edad>=30:
    print("Adulto/a: mayor o igual que 30 años.")

#Ejercicio 5

password = input("Introduzca una contraseña de 8 a 14 caracteres: ")

if len(password)>=8 and len(password)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

from statistics import mode, median, mean
import random

num_aleatorios = [random.randint(1, 100) for i in range (50)]

if (mean(num_aleatorios)>median(num_aleatorios)) and (median(num_aleatorios)>mode(num_aleatorios)):
    print("Sesgo positivo o a la derecha")
elif (mean(num_aleatorios)<median(num_aleatorios) and median(num_aleatorios)<mode(num_aleatorios)):
    print("Sesgo negativo o a la izquierda")
elif (mode(num_aleatorios) == median(num_aleatorios)) and (mode(num_aleatorios)==mean(num_aleatorios)):
    print("Sin sesgo")

#Ejercicio 7

texto = input("Ingrese un texto o una frase: ")
agrega = "?"
ultimo = texto[len(texto)-1]
if (ultimo == "a" or ultimo == "e" or ultimo == "i" or ultimo == "o" or ultimo == "u" or
    ultimo == "A" or ultimo == "E" or ultimo == "I" or ultimo == "O" or ultimo == "U"):
    texto = texto+"!"
print(texto)

#Ejercicio 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese entre la opción 1, 2 o 3: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Esa opción no existe")

#Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud<3:
    print("Muy leve")
elif magnitud>=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte")
elif magnitud>=7:
    print("Extremo")

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