#EJERCICIO 1
saludo = "Mundo"
print("Hola " + saludo + "!")

#EJERCICIO 2
nombre = input("Ingresa tu nombre: ") #ejercicio 2
print(f"Hola {nombre}")

#EJERCICIO 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
residencia = input("Ingresa tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#EJERCICIO 4
radio = float(input("Ingresa el radio: "))
area = 3.14 * (radio **2)
perimetro = 2 * 3.14 * radio

print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

#EJERCICIO 5
cant_de_segundos = int(input("Ingresa la cantidad de segundos: "))
calcular_horas = cant_de_segundos // 3600
print(f"{cant_de_segundos} segundos equivalen a {calcular_horas} horas.")


#EJERCICIO 6
numero = int(input("Ingrese un numero para ver la tabla de multiplicar: "))
print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")

#EJERCICIO 7
print("**Ingresa numeros distintos de Cero**")
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Division: {num1 // num2}") 

#EJERCICIO 8
altura = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kg: "))
masa_corporal= peso / altura**2
print(f"Su IMC es: {masa_corporal}")

#EJERCICIO 9
valor_Celsius = int(input("Ingresa un valor en celsius: "))
valor_en_fahrenheit = (valor_Celsius * 9/5) + 32
print(f"{valor_Celsius}ºC, equivalen a {valor_en_fahrenheit}ºF")

#EJERCICIO 10
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

suma = num1 + num2 + num3
promedio = suma / 3
print(f"El promedio total es: {promedio}") 