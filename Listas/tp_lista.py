#EJERCICIO 1
lista_numeros = list(range(1,101))
lista_multiplos_de_4 = []
for i in range(1, len(lista_numeros)):
    if lista_numeros[i] % 4 == 0:
        lista_multiplos_de_4.append(lista_numeros[i])
        
print(lista_multiplos_de_4)



#EJERCICIO 2
lista_elementos = ["Programacion", "Musica", "Piano", "Viajes", "Amigos"]

print(lista_elementos[-2])


#EJERCICIO 3
lista = []

lista.append("Juegos")
lista.append("Paisajes")
lista.append("Joel")

print(lista)


#EJERCICIO 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#EJERCICIO 5
#Saca de la lista el numero(elemento) mas grande en cantidad


#EJERCICIO 6
num_lista = list(range(10,31,5))
print(num_lista[:2])


#EJERCICIO 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "ford"
autos[2] = "BMW"
print(autos)


#EJERCICIO 8
dobles = []
valor_5 = 5*2
valor_10 = 10*2
valor_15 = 15*2
dobles.append(valor_5)
dobles.append(valor_10)
dobles.append(valor_15)
print(dobles)

#EJERCICIO 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
print(f"Lista: {compras}")
print("- Agregar jugo")
compras[2].append("jugo")

print("- Remplazar fideos por tallarines")
compras[1][1] = "tallarines"

print("- Eliminar pan de la lista")
compras[0].remove("pan")

print("- Imprimir la lista resultante por pantalla")
print(compras)


#EJERCICIO 10
lista_anidada = [0, 1, [25.5, 57.9, 30.6], False]
print(lista_anidada)
