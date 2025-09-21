
#EJERCICIO A
nombre = input("Ingresa tu nombre: ")
edad = int(input(f"Ingresa tu edad, **{nombre}**: "))
print(f"Hola {nombre}!")

dato1 = input("Has ido a la facultad (si/no): ")
dato2 = input(f"Tomaste la media-tarde (si/no): ")

print("Resumen del dia: ")
print(f"·Nombre: {nombre}")
print(f"·Edad: {edad}")
print(f"·Hoy fue a la universidad: {dato1}")
print(f"·Tomo la media-tarde: {dato2}")


#EJERCICIO B
largo = float(input("Ingresa el largo de la mesa en metros: "))
ancho = float(input("Ingresa el ancho de la mesa en metros: "))

mantel = largo * ancho

print(f"Necesitas un mantel de {mantel} metros cuadrados para cubrir la mesa.")



#EJERCICIO C
minutos = int(input("Ingresa una cantidad en minutos: "))
a_horas = minutos // 60
minutes = minutos % 60
print(f"{minutos} minutos, equivalen a {a_horas} horas y {minutes} minutos.")

#CONDICIONALES
#EJERCICIO A
velocidad = float(input("Ingresa la velocidad a la que viaja(en km/h): "))
if 40 >= velocidad:
    print("Usted va lento")
elif 120 < velocidad:
    print("Usted va rapido")
else:
    print("Usted va normal")
  
#EJERCICIO B
edad = int(input("Ingresa tu edad: "))
mayor_de_Edad = edad >= 18
mensaje_tipo_edad = ""
mostrar = ""
mensaje_positivo = ". ¡¡Felicidades!! tu vida esta dando buenos resultados." 

es_un_trabajador = input("¿Trabajas?: ")

pasatiempo = input("¿Cual es tu pasatiempo?: ")
if mayor_de_Edad:
    mensaje_tipo_edad = " mayor de edad "
    if es_un_trabajador.capitalize() == "Si":
        trabajo = input("¿De que trabajas?: ")
        mostrar = "Eres " + mensaje_tipo_edad + ". Estas trabajando de " + trabajo + " y tu pasatiempo es " + pasatiempo + mensaje_positivo 
    elif es_un_trabajador.capitalize() == "No":
        mostrar = "Eres " + mensaje_tipo_edad + ". No Estas trabajando y tu pasatiempo es " + pasatiempo + ". ¡¡Recomendacion!! Conseguite un trabajo**." 
else:
    mensaje_tipo_edad = " menor de edad "
    if es_un_trabajador.capitalize() == "Si":
        trabajo = input("¿De que trabajas?: ")
        mostrar = "Eres " + mensaje_tipo_edad + ". Estas trabajando de " + trabajo + " y tu pasatiempo es " + pasatiempo + mensaje_positivo
    elif es_un_trabajador.capitalize() == "No":
        mostrar = "Eres " + mensaje_tipo_edad + ". No Estas trabajando y tu pasatiempo es " + pasatiempo + ". ¡¡Recomendacion!! Conseguite un trabajo**. Se que sos menor,pero los mejores resultados se buscan desde lo pequeño" 
    
print(mostrar)

#EJERCICIO C
num = int(input("Ingresa un numero: "))
if num % 2 == 0:
    print(f"El numero {num} es Par.")
else:
    print(f"El numero {num} es Impar.")


#ESTRUCTURAS REPETITIVAS
#EJERCICIO A
for i in range(1,11):
    print(i)

#EJERCICIO B
contador_num = 0
suma = 0
while True:
    contador_num = contador_num + 1
    if contador_num == 101:
        break
    else:
        suma = suma + contador_num

print(f"La suma total de todos los numero del 1 al 100 es: {suma}")


#EJERCICIO C
num = int(input("Ingresa un numero para ver su tabla de multiplicar: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")


#BUCLES CON CONDICIONALES
#EJERCICIO A
suma = 0
while True:
    pedir_num = int(input("Ingresa un numero: "))
    
    if pedir_num != 0:
        suma = suma + pedir_num
    else:
        break
print(f"La suma de todos lo numeros ingresados es {suma}")


#EJERCICIO B
clave = "Joel1234."
while True:
    pedir_clave = input("Ingresa tu contraseña: ")
    
    if pedir_clave == clave:
        break
    else:
        print("**Contraseña Incorrecta**")
        continue
print("##Contraseña Correcta##")


#EJERCICIO C
import random

num_aleatorio = random.randint(1,10)
while True:
    num_ingresado = int(input("Ingresa el numero: "))
    if num_ingresado == num_aleatorio:
        break
    elif num_ingresado < num_aleatorio:
        print("El numero es mas grande")
    elif num_ingresado > num_aleatorio:
        print("El numero es mas pequeño")
    
print(f"Adivinaste. El numero es {num_aleatorio}")


#LISTAS
#EJERCICIO A
lista = ["Joel", "Juan", "Luz", "Camila", "Lautaro"]

print(f"Primer elemento de la lista: {lista[0]}")
print(f"Ultimo elemento de la lista: {lista[-1]}")


#EJERCICIO B
lista_nueva = [10 , 15, 20, 30, 40]
lista_nueva[2] = 99
print(f"Lista: {lista_nueva}")

#EJERCICIO C
lista = [7, 42, 15, 3, 28, 91, 54]
print(lista[:3])
print(lista[-2:])

#EJERCICIO D
print("Ingresa 3 frutas: ")
lista = []
for i in range(1,4):
    fruta = input(f"Ingresa la fruta {i}: ")
    lista.append(fruta)
    
print(f"La lista con las frutas ingresadas: {lista}")

#EJERCICIO E
matriz = [
    [2,4,6],
    [7,8,9]
]

print(matriz[0][1])
print(matriz[1][0])
print(matriz[1][2])


#EJERCICIO F

numeros = [5, -2, 8, -7, 1, 3]


print("Números positivos:")
for n in numeros:
    if n > 0:
        print(n, end=" ")

print("\n")  


print("Números negativos:")
for n in numeros:
    if n < 0:
        print(n, end=" ")


#EJERCICIO ULTIMO
# Mini Proyecto: Tienda de ropa

prendas = ["camisa", "remera"]
stock = [2,4]

while True:
    print("\n--- Menú Tienda de Ropa ---")
    print("1. Ingresar prendas y stock")
    print("2. Ver inventario")
    print("3. Ver prendas agotadas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        
        nombre = input("Nombre de la prenda: ")
        cantidad = int(input("Cantidad disponible: "))
        prendas.append(nombre)
        stock.append(cantidad)
        print(f" {nombre} agregada con stock {cantidad}")

    elif opcion == "2":
        
        if prendas:
            print("\n--- Inventario ---")
            for i in range(len(prendas)):
                print(f"{prendas[i]} → {stock[i]} unidades")
        else:
            print("No hay prendas cargadas.")

    elif opcion == "3":
        
        print("\n--- Prendas agotadas ---")
        agotadas = False
        for i in range(len(prendas)):
            if stock[i] == 0:
                print(f"{prendas[i]} está agotada ")
                agotadas = True
        if not agotadas:
            print("No hay prendas agotadas ")

    elif opcion == "4":
        print(" Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
