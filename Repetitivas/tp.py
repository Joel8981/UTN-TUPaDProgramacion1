#EJERCICIO 1
for i in range(101):
    print(i)
    
#EJERCICIO 2
num = int(input("Ingresa un numero: "))
digitos = 0

if num == 0:
    digitos = 1
else:
    
    while num != 0:
        num = num // 10
        digitos = digitos + 1
    
print(f"Tiene {digitos} digitos")




#EJERCICIO 3
num_Inicio = int(input("Ingresa un numero de inicio: "))
num_Final = int(input("Ingresa un numero de fin: "))
suma = 0

valorInicial = 0
valorFinal = 0
if num_Inicio < num_Final:
    valorInicial = num_Final
    valorFinal = num_Inicio
else:
    valorInicial = num_Inicio
    valorFinal = num_Final
    
for i in range(valorInicial + 1, valorFinal):
    suma = suma + i
  

print(f"El resultado de la suma es: {suma}")


#EJERCICIO 4
num=1
suma=0
while (num != 0):
    num= int(input("ingresa un numero: "))
    if num > 0:
      suma= suma + num
      
print(f"la suma de los numeros ingresados es: {suma}")



#EJERCICIO 5
import random

print("**Adivina el numero**")
contador_intentos = 0
num_aleatorio = random.randint(0,9)
while True:
    num_para_adivinar = int(input("Ingresa el numero que crees que es: "))
    if num_para_adivinar == num_aleatorio:
        break
    contador_intentos = contador_intentos  + 1

print(f"Adivinaste, el numero es {num_aleatorio}")
print(f"Se realizo {contador_intentos} intentos.")
    
#EJERCICIO 6 
for i in range(100,-1,-1):
    if i % 2 != 0:
        continue
    print(i)
    
    
#EJERCICIO 7
pedir_numero = int(input("Ingresa hasta que numero quieres sumar: "))
suma = 0
for i in range(0,pedir_numero+1):
    if pedir_numero < 0:
        break
    suma = suma + i
print(f"La suma de todos los numeros desde 0 hasta {pedir_numero} es: {suma}")


#EJERCICIO 8
contadorPositivo = 0
contadorNegativo = 0
contadorPar = 0
contadorImpar = 0

for i in range(1, 101):
    num = int(input(f"Ingresa el numero {i}:"))
    
    if num % 2 == 0:
        contadorPar = contadorPar + 1
    else:
        contadorImpar = contadorImpar + 1
    if num > 0:
        contadorPositivo = contadorPositivo + 1
    else:
        contadorNegativo = contadorNegativo + 1

print(f"Numeros positivos: {contadorPositivo}")
print(f"Numero negativos: {contadorNegativo}")
print(f"Numeros Pares: {contadorPar}")
print(f"Numeros Impares: {contadorImpar}")


#EJERCICIO 9
suma = 0
media = 0

for i in range(1,101):
    num_a_ingresar = int(input(f"Ingresa un numero {i}: "))
    suma = suma + num_a_ingresar
    

media = suma / 100

print(f"La media de los valores ingresados es: {round(media, 1)}")

#EJERCICIO 10
numero = int(input("Ingresa un numero: "))
invertir = 0

digito = 0
while numero > 0:
    digito = numero % 10
    invertir = invertir * 10 + digito
    numero = numero // 10
    
print(invertir)