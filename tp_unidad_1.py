#Ejercicio 1
print("Hola Mundo")

#Ejercicio 2
nombre= input("Ingresa tu nombre:")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre=input("Ingrese su nombre ")
apellido=input("Ingrese su apellido ")
edad=input("Ingrese su edad ")
residencia=input("Ingrese su pais de residencia ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
r = float(input("Ingrese el radio del círculo: "))
a = 3.14*r
p = 2*3.14*r
print(f"El area del circuclo es {a} y el perimetro es {p}")

#Ejercicio 5
s = int(input("Ingrese cantidad de segundos para transformar a hora "))
h = (s/60)/60
print(f"La cantidad de segundos ingresada equivale a {h} horas")

#Ejercicio 6
n = int(input("Ingresa un número para mostrar la tabla de multiplicar hasta el 9: "))
print(n, "x 1 =", n * 1)
print(n, "x 2 =", n * 2)
print(n, "x 3 =", n * 3)
print(n, "x 4 =", n * 4)
print(n, "x 5 =", n * 5)
print(n, "x 6 =", n * 6)
print(n, "x 7 =", n * 7)
print(n, "x 8 =", n * 8)
print(n, "x 9 =", n * 9)

#Ejercicio 7
numero1 = int(input("Ingresa el primer número (distinto de 0): "))
numero2 = int(input("Ingresa el segundo número (distinto de 0): "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2  


print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#Ejercicio 8
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso/(altura)**2
print(f"Tu IMC es: {imc}")

#Ejercicio 9
temp = float(input("Ingrese la temperatura en celsius: "))
faren = (temp*9/5)+32
print(f"El equivalente en celsius es: {faren} C")

#Ejercicio 10

num1 = float(input("Ingrese el primer número "))
num2 = float(input("Ingrese el segundo número "))
num3 = float(input("Ingrese el tercer número "))

prom = (num1+num2+num3)/3

print(f"El promedio es: {prom}")