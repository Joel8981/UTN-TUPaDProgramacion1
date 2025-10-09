#EJERCICIO 1

# - - Funcion
def imprimir_hola():
    print("Hola Mundo")
    
# - - Programa principal
imprimir_hola()


#EJERCICIO 2
# - - Funcion
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# - - Programa principal 
name = input("Ingresa tu nombre: ")
print(saludar_usuario(name))


#EJERCICIO 3
# - - Funcion
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}"    

#Programa principal
pedir_nombre = input(" - Ingresa tu nombre: ")
pedir_apellido = input(" - Ingresa tu apellido: ")
pedir_edad = int(input(" - Ingresa tu edad: "))
pedir_residencia = input(" - Ingresa tu residencia: ")

print(informacion_personal(pedir_nombre, pedir_apellido, pedir_edad, pedir_residencia))



#EJERCICIO 4
# - - Funciones
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Programa principal
r = float(input("Ingresa el radio del circulo: "))

print(f" - El area  es {round(calcular_area_circulo(r), 1)}")
print(f" - El perimetro es {round(calcular_perimetro_circulo(r), 1)}")


#EJERCICIO 5
# - Funcion
def segundos_a_horas(segundos):
    return segundos // 3600

#Programa principal
s = int(input("Ingresa una cantidad de segundos: "))

if s >= 3600:
    print(f"{s} segundos equivalen a {segundos_a_horas(s)} hora/s")


#EJERCICIO 6
# - Funcion
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f" {numero} x {i} = {numero*i}")
    
#Programa principal
num = int(input("Ingresa tu numero para ver su tabla de multiplicar: "))

print(tabla_multiplicar(num))


#EJERCICIO 7
# - Funcion
def operaciones_basicas(a, b):
    print(f"Sumar {a} y {b} = {a+b}")
    print(f"Restar {a} y {b} = {a-b}")
    print(f"Multiplicar {a} y {b} = {a*b}")
    print(f"Dividir {a} y {b} = {a//b}")
    
    
#Programa principal
a = 10
b = 2
operaciones_basicas(a, b)


#EJERCICIO 8
def imc(peso, altura):
    return peso / altura**2

#Programa principal
p_en_kg = float(input("Ingresa tu peso en kg: "))
a_en_metros = float(input("ingresa tu altura en metros: "))

print(f"Su IMC es {round(imc(p_en_kg, a_en_metros), 1)}")


#EJERCICIO 9
# - Funcion
def celsius_a_farenheit(celsius):
    return (celsius * 9/5 ) + 32

#Programa principal
c = float(input("Ingresa un valor en Celsius: "))
print(f"{c}° C, equivalen a {celsius_a_farenheit(c)}°F")


#EJERCICIO 10
# - Funcion
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal 
a = float(input("Ingresa numero A: "))
b = float(input("Ingresa numero B: "))
c = float(input("Ingresa numero C: "))

print(f"El promedio de los 3 numeros ingresados es: {round(calcular_promedio(a, b, c), 1)}")