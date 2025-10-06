# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a+b+c)/3

a = float(input('Ingrese el primer número: '))
b = float(input('Ingrese el segundo número: '))
c = float(input('Ingrese el tercer número: '))

print(f'El promedio es {calcular_promedio(a, b, c)}')