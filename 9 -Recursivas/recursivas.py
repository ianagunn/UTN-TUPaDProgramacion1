#Ejercicio 1
def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num-1)

num = int(input("Ingrese un numero factorial: "))

for i in range(1, num+1):
    print(factorial(i))

#Ejercicio 2
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1)+fibonacci(posicion-2)
    
posicion = int(input("Ingrese la posición del numero: "))

for i in range(posicion+1):
    print(fibonacci(i))

#Ejercicio 3
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m-1)
    
n = int(input("Ingrese el número de la base: "))
m = int(input("Ingrese el número del exponente: "))

resultado = potencia(n, m)

print(f"\n{m} elevado a {n} tiene como resultado {resultado}\n")

#Ejercicio 4
def decimal_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    else:
        return decimal_binario(n // 2) + str(n % 2)
    
num = int(input("Ingrese un número entero y positivo: "))
binario = decimal_binario(num)
print(f"El número {num} en binario es: {binario}")

#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print(es_palindromo(texto))

#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(2))

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2))