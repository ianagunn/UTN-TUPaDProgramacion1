#Ejercicio 1
for x in range (101):
    print(x)

#Ejercicio 2
num = int(input("Ingrese un numero entero: "))
i=0  
if num == 0:
    i = 1
while num > 0:
    num = num//10
    i+=1
print(i)

#Ejercicio 3
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma=0

if num1 < num2:
    for i in range(num1 + 1, num2):
        suma += i
else:
    for i in range(num2 + 1, num1):
        suma += i
print(suma)

#Ejercicio 4
num = int(input("Ingrese un numero para sumar: "))
suma=0

while num > 0:
    suma+=num
    num = int(input("Ingrese un numero para sumar: "))
print("La suma es: ", suma)

#Ejercicio 5
import random
num = random.randint(0,9)
i = 1
print(num)
x = int(input("Adivine el numero aleatorio: "))

if x == num:
    print("Adivinaste en ", i, " intento" )
else:
    while x != num:
        x = int(input("Adivine el numero aleatorio: "))
        i+=1
    print("Adivinaste en", i, "intentos" )

#Ejercicio 6
for i in range(100, -1, -2):
    print(i)

#Ejercicio 7
num = int(input("Ingrese un numero: "))
suma=0

if num>0:
    for i in range(num+1):
        suma += i
    print(suma)
else:
    print("El numero ingresado debe ser positivo")

#Ejercicio 8
cantidad = 100
positivo=0
negativo=0
par=0
impar=0

for i in range(cantidad):
    num = int(input("Ingrese un numero: "))

    if num>0:
        positivo+=1
    else:
        negativo+=1
    
    if num%2==0:
        par+=1
    else:
        impar+=1

print("Numeros positivos:", positivo)
print("Numeros negativo:", negativo)
print("Numeros par:", par)
print("Numeros impar:", impar)

#Ejercicio 9
cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input("Ingrese un numero: "))
    suma += num

media = suma/cantidad
print("La media de los numeros ingresados es:", media)

#Ejercicio 10
num = int(input("Ingrese un numero: "))
inv=0

while num > 0:
    digito = num%10
    inv = digito+inv*10
    num //= 10
print("El numero invertido es: ", inv)