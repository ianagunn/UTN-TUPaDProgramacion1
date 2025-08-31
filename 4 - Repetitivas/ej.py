num = int(input("Ingrese un numero: "))
inv=0

while num > 0:
    digito = num%10
    inv = digito+inv*10
    num //= 10
print("El numero invertido es: ", inv)