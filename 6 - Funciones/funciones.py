#Ejercicio 1
def imprimir_hola_mundo():
    print('Hola Mundo!')

imprimir_hola_mundo()

# Ejercicio 2
def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

nombre = input('Ingrese su nombre por favor: ')
saludar_usuario(nombre)

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido} y tengo {edad} años y vivo en {residencia}')

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input("Ingrese su edad: ")
residencia = input('Ingrese su residencia: ')
informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4
pi = 3.1416
def calcular_area_circulo(radio):
    return pi*(radio)**2

def calcular_perimetro_circulo(radio):
    return 2*pi*radio
    

radio = input('Ingrese el radio del circulo que desea obtener área y perimetro: ')
radio = float(radio)

if radio > 0:

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f'El area es {area}')
    print(f'El perimetro es {perimetro}')
else:
    print('El radio ingresado debe ser mayor a 0')

# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos/3600

segundos = int(input('Ingrese la cantidad de segundos que desea convertir en horas: '))
if segundos > 0:
    horas = segundos_a_horas(segundos)

    print(f'La conversion de segundos equivale a {horas} horas')
else:
    print('Ingrese una cantidad de segundos mayor a 0')
    
# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(i*numero) 

numero = int(input('Ingrese un numero: '))

if numero > 0:
    tabla_multiplicar(numero)

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return(suma, resta, multiplicacion, division)


a = int(input('\n Ingrese el primer número: '))
b = int(input('\n Ingrese el segundo número: '))

resultados = operaciones_basicas(a, b)

print('\n ----- Los resultados obtenidos son -----')
print(f'\n La sumatoria entre el primer y segundo número es: {resultados[0]}')
print(f'\n La resta entre el primer y segundo número es: {resultados[1]}')
print(f'\n La multiplicación entre el primer y segundo número es: {resultados[2]}')
print(f'\n La división entre el primer y segundo número es: {resultados[3]}')

# Ejercicio 8
def calcular_imc(peso, altura):
    return(peso/(altura**2))

peso = float(input('Ingrese su peso: '))
altura = float(input('Ingrese su altura: '))

imc = calcular_imc(peso, altura)

print(f'Tu IMC es {imc}')

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius+32

celsius = int(input('Ingresa la temperatura en grados celsius: '))
print(f'La temperatura ingresada equivale a {celsius_a_fahrenheit(celsius)} fahrenheit')

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a+b+c)/3

a = float(input('Ingrese el primer número: '))
b = float(input('Ingrese el segundo número: '))
c = float(input('Ingrese el tercer número: '))

print(f'El promedio es {calcular_promedio(a, b, c)}')