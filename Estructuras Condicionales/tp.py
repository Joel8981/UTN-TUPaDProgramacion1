#EJERCICIO 1
edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= 18:
    print("Es mayor de edad")

#EJERCICIO 2
nota_usuario = float(input("Ingresa tu nota: "))

if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
#EJERCICIO 3
num = int(input("Ingresa un numero entero: "))

if num % 2 == 0:
    print("Has ingresado un nùmero par")
else:
    print("Por favor, ingrese un numero par")
    
#EJERCICIO 4
edad_persona = int(input("Ingresa tu edad: "))

edad_valida = edad_persona > 0

if edad_valida:
    if edad_persona < 12:
        print("Niño/a")
    elif edad_persona < 18:
        print("Adolescente")
    elif edad_persona < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")
else:
    print("edad no valida")
    
#EJERCICIO 5
clave = input("Ingresa una contraseña: ")

longitud_clave_ingresada= len(clave)
clave_valida = (longitud_clave_ingresada >= 8) and (longitud_clave_ingresada <= 14)
if clave_valida:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#EJERCICIO 6
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print(mode(numeros_aleatorios))
print(median(numeros_aleatorios))
print(mean(numeros_aleatorios))

#EJERCICIO 7
frase = input("Ingresa una frase o palabra: ")
ultima_letra = len(frase) - 1
if (frase[ultima_letra] == "a") or (frase[ultima_letra] == "e") or (frase[ultima_letra] == "i") or (frase[ultima_letra] == "o") or (frase[ultima_letra] == "u"):
    print(f"{frase}!")
else:
    print(frase)
    
#EJERCICIO 8
nombre = input("Ingrese su nombre: ")
num = int(input("Ingrese un numero: "))

num_valido = num > 0 and num <= 3

if num_valido:
    if num == 1:
        print(nombre.upper())
    elif num == 2:
        print(nombre.lower())
    else:
        print(nombre.title())
else:
    print("numero invalido, solo los numeros 1, 2 y 3 son validos")
    
#EJERCICIO 9
magnitud_terremoto = float(input("Ingresa el valor de magnitud segun la escala de Richter: "))

print("Magnitud: ", end="")

valor_valido = magnitud_terremoto > 0

if valor_valido:
    if magnitud_terremoto < 3:
        print("Muy Leve")
    elif magnitud_terremoto < 4:
        print("Leve")
    elif magnitud_terremoto < 5:
        print("Moderado")
    elif magnitud_terremoto < 6:
        print("Fuerte")
    elif magnitud_terremoto < 7:
        print("Muy fuerte")
    else:
        print("Extremo")
else:
    print("el valor debe ser mayor a 0")
    
#EJERCICIO 10
print("**ESTACIONES DEL AÑO SEGUN EL HEMISFERIO**")
print("- Letra N: Hemisferio Norte")
print("- Letra S: Hemisferio Sur")
hemisferio = input("Ingresa la letra segun el hemisferio: ")

num_dia = int(input("Ingresa el numero de dia: "))
mes = int(input("Ingresa el numero de mes: "))

meses_validos = mes > 0 and mes <= 12
dias_validos = num_dia > 0 and num_dia <= 31 

estacion_1 = ((mes == 1 or mes == 12) and num_dia <= 31) or (mes == 2 and num_dia <= 28) or (mes == 3 and num_dia <= 20)
estacion_2 = (mes == 3 and num_dia >= 21) or (mes == 5 and num_dia <= 31) or (mes == 4 and num_dia <= 30) or (mes == 6 and num_dia <= 20)
estacion_3 = (mes == 6 and num_dia <= 30) or ((mes == 7 or mes == 8) and num_dia <= 31) or (mes == 9 and num_dia <= 20)
estacion_4 = ((mes == 9 or mes == 11) and num_dia <= 30) or (mes == 10 and num_dia <= 31) or (mes == 12 and num_dia <= 20)

if (hemisferio == "N" and meses_validos) and dias_validos:
    print("Usted esta en: ", end="")
    if estacion_1:
        print("Invierno")
    elif estacion_2:
        print("Primavera")
    elif estacion_3:
        print("Verano")
    elif estacion_4:
        print("Otoño")
elif (hemisferio == "S" and meses_validos) and dias_validos:
    print("Usted esta en: ", end="")
    if estacion_1:
        print("Verano")
    elif estacion_2:
        print("Otoño")
    elif estacion_3:
        print("Invierno")
    elif estacion_4:
        print("Primavera")
else:
    if hemisferio != "N" or hemisferio != "S":
        print("Error, la letra no corresponde a un hemisferio")
    else:
        print("Error, el valor del dia o mes no esta en el rango")