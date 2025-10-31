#EJERCICIO 1
def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        return n*calcular_factorial(n-1)
    

num = int(input("Ingresa el numero para calcular el factorial: "))

if num >=0:
    for i in range(num+1):
        print(f"El factorial de {i} es: {(calcular_factorial(i))}")
else:
    print("No se puede calcular con numeros negativos")
   

#EJERCICIO 2
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("¿Hasta que numero mostrar la serie fibonacci? : "))

print((fibonacci(num)))
    



#EJERCICIO 3
def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * calcular_potencia(base, exponente-1)
    
b = int(input("Ingresa la base: "))
x = int(input("Ingresa el exponente: "))

print(f"El resultado es {(calcular_potencia(b,x))}")


#EJERCICIO 4
def en_binario(n):
    if n == 0:
        return "0"
    elif n // 2 != 0:
        return en_binario(n // 2) + str(n % 2)
    else:
        return str(n % 2)
        

num = int(input("Ingresa un numero para expresarlo en binario: "))

if num >= 0:
    print(f" - Numero: {num}  | Binario: {(en_binario(num))}")
else:
    print("Los numeros deben ser positivos")


#EJERCICIO 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    
    return es_palindromo(palabra[1: -1])

p = input("Ingresa una palabra: ")

if es_palindromo(p):
    print("Es palindromo")
else:
    print("No es palindromo")




#EJERCICIO 6
def suma_digitos(n):
    
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
num = int(input("Ingresa el numero: "))

print(f"La suma de los digitos es: {(suma_digitos(num))}")


#EJERCICIO 7
def contar_bloques(n):
    if n < 0:
        return 0
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
        
    

cant_bloques = int(input("Ingresa un numero de bloques para la base: "))

print(f"Piramide con base {cant_bloques} : {(contar_bloques(cant_bloques))}")




#EJERCICIO 8
def contar_digito(numero, digito):
    
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        
        si_coincide = 0
        
        if ultimo_digito == digito:
            si_coincide = 1
        
        
        numero_sin_ultimo_digito = numero // 10
        
        return si_coincide + contar_digito(numero_sin_ultimo_digito, digito)
    

    
    
numero = int(input("Ingresa un numero positivo: "))

digito = int(input("Ingresa el digito a contar: "))

print(f"El numero {numero} aparece : {(contar_digito(numero, digito))} veces")    
