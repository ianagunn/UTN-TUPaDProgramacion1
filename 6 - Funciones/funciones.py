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
# Ejercicio 7
# Ejercicio 8
# Ejercicio 9
# Ejercicio 10
