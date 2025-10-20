
# 1)

#Creamos el diccionarios con sus keys y values
precio_frutas = {
    "Banana": 1200,
    "Anana": 1500,
    "Melon": 3000,
    "Uva": 1450 
}

#    Agregamos keys(nombre de la fruta) y values(precio)
precio_frutas["Naranja"] = 1200
precio_frutas["Manzana"] = 1500
precio_frutas["Pera"] = 2300

#Mostramos el diccionario
print(precio_frutas)


# 2)
#Con el mismo ejemplo del anterior actualizamos sus precios(values)
print("  - - Diccionario actualizado  - -  ")
precio_frutas["Banana"] = 1330
precio_frutas["Manzana"] = 1500
precio_frutas["Melon"] = 2800

#Mostramos el resultado
print(precio_frutas)

# 3)
#Crear una lista a partir del diccionario precios_frutas

#Crear lista con las keys del diccionario
print("  - - Lista con las frutas del diccionario  - -  ")
lista_frutas = list(precio_frutas.keys())

#Mostramos la lista nueva
print(lista_frutas)


# 4)

#Creamos un diccionario vacio
dic_consultar_numeros_telefonicos = dict()

#Creamos un bucle for para llenar el diccionario
for i in range(5):
    nombre = input(f" - Ingresa tu nombre del contacto {i+1}: ")
    numero_telefonico = input("Ingresa tu numero telefonico: ")
    dic_consultar_numeros_telefonicos[nombre] = numero_telefonico
    

#Mostramos el diccionario
print(dic_consultar_numeros_telefonicos)

#Le pedimos que ingres un nombre a buscar
buscar_nombre = input("Ingresa el nombre que queres buscar del diccionario de contactos: ")

#Condicional para buscar el nombre
if buscar_nombre in dic_consultar_numeros_telefonicos:
    print(f"{buscar_nombre} : {dic_consultar_numeros_telefonicos[buscar_nombre]}")
else:
    print("El contacto no existe")
    



#EJERCICIO 5
#Creamos una variable para pedirle una frase
frase  = input("Ingresa una frase: ")

#En otra variable transformamos la frase en conjunto
conjunto = set(frase.split())

#Mostramos el conjunto
print(f"Conjunto de palabras: {conjunto}")

#En otra separamos cada palabra de la frase como cadenas independientes
palabras = frase.split()

#Creamos un diccionario vacio
diccionario = dict()
#Recorremos con un for y agregamos al diccionario
for palabra in set(palabras):
    diccionario[palabra] = palabras.count(palabra)
    
#Imprimimos el diccionario
print(diccionario)


#EJERCICIO 6

#CREAMOS UNA LISTA Y UN DICCIONARIOS
lista = list()
alumnos = dict()

#CON UN BUCLE FOR PEDIMOS LOS NOMBRES DE 3 ALUMNOS
for i in range(3):
    alumn = input(f" -Ingresa el nombre del alumno {i+1}: ")
    
    print(alumn)
    #CON ESTE BUCLE RELLENAMOS LAS 3 NOTAS EN UNA LISTA DE CADA ALUMNOS
    for nota in range(3):
        
        nota = int(input(f"Nota {nota+1}: "))
        lista.append(nota)
        
    
    #CON ESTA FUNCION TRANSFORMAMOS LA LISTA EN UNA TUPLA 
    #LIMPIAMOS LA LISTA PARA EVITAR REPETICIONES
    tupla = tuple(lista)
    lista.clear()
    
    #LO AGREGAMOS AL DICCIONARIO
    alumnos[alumn] = tupla
        
        

#MOSTRAMOS EL DICCIONARIO
print(f"Diccionario: {alumnos}")
        
#CON OTRO BUCLE MOSTRAMOS LOS PROMEDIOS
for c_alumno, notas in alumnos.items():
    print(f" - {c_alumno}; Promedio: {round(sum(notas) / 3, 1)}")




#EJERCICIO 7

#CREAMOS 2 CONJUNTOS
parcial_1 = {"Jose", "Joel", "Lautaro", "Juan"}
parcial_2 = {"Sofia", "Pedro", "Jose", "Oriana"}

#APROBARON AMBOS (INTERSECCION)
ambos = parcial_1 & parcial_2
print("Aprobaron ambos parciales:", ambos)

#APROBO SOLO UNO > diferencia simetrica
solo_uno = parcial_1 ^ parcial_2
print("Aprobaron solo uno de los parciales:", solo_uno)

#APROBO AL MENOS UNO (UNION)
al_menos_uno = parcial_1 | parcial_2
print("Aprobaron al menos un parcial:", al_menos_uno)



# EJERCICIO 8
# DICCIONARIO DE TIENDA
diccionario_tienda = {
    "Gaseosa": 3, 
    "Agua Mineral": 4
}

while True:
    # MENU DE OPCIONES
    print("\n - - MENU DE OPCIONES - - ")
    print("1. Consultar el stock de un producto")
    print("2. Agregar unidades de producto")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    print()
    
    # SELECCION DE OPCION
    opc = int(input("Ingresa el numero de opcion: "))
    
    # OPCION 1: CONSULTAR STOCK
    if opc == 1:
        print("\n - CONSULTAR STOCK DE PRODUCTO EXISTENTE -")
        name_product = input("Ingresa el nombre del producto a consultar: ")
        
        if name_product in diccionario_tienda:
            unidades = diccionario_tienda[name_product]
            print(f"Producto: {name_product} | Unidades en stock: {unidades}")
        else:
            print("Disculpa.. El producto no existe en la tienda.")
    
    # OPCION 2: AGREGAR UNIDADES
    elif opc == 2:
        print("\n - AGREGAR UNIDADES A UN PRODUCTO -")
        name = input("Ingresa el nombre del producto: ")
        
        if name in diccionario_tienda:
            stock = int(input("Ingresa la cantidad a agregar: "))
            diccionario_tienda[name] += stock
            print(f" Stock actualizado. Nuevo stock de {name}: {diccionario_tienda[name]}")
        else:
            print("El producto no existe..")
    
    # OPCION 3: AGREGAR NUEVO PRODUCTO
    elif opc == 3:
        print("\n - AGREGAR NUEVO PRODUCTO -")
        nuevo_producto = input("Ingresa el nombre del nuevo producto: ")
        stock = int(input("Ingresa el stock inicial: "))
        
        diccionario_tienda[nuevo_producto] = stock
        print(f" Producto agregado: {nuevo_producto} ({stock} unidades)")
    
    # OPCION 4: SALIR
    elif opc == 4:
        print("\nSaliendo del programa... ")
        break
    
    else:
        print("Opción no válida. Por favor, intentá de nuevo.")

    # MOSTRAR STOCK ACTUAL (opcional)
    print("\nStock actual de la tienda:", diccionario_tienda)



#EJERCICIO 9
# Creamos la agenda
agenda = {
    ("Lunes", "08:00"): "Clase de matemáticas",
    ("Lunes", "10:00"): "Reunión con el equipo de programación",
    ("Martes", "14:00"): "Práctica de piano",
    ("Miércoles", "09:00"): "Ejercicio físico",
    ("Viernes", "18:00"): "Salida con amigos"
}

# Mostrar toda la agenda
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# Acceder a un evento específico
evento_especifico = agenda.get(("Martes", "14:00"))
print("\nEvento del Martes a las 14:00:", evento_especifico)


#EJERCICIO 10
# Diccionario original: países → capitales
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Invertir el diccionario: capitales → países
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print(capitales_paises)

