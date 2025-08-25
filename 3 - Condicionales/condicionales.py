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