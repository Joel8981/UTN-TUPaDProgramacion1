#EJERCICIO A
lista_nombre = ["Nahuel", "Joaquin", "Marcos", "Lucas", "Matias"]
print(f"- Primer elemento de la lista **{lista_nombre[0]}** \n - Ultimo elemento de la lista **{lista_nombre[-1]}**")


#EJERCICIO B
lista_numeros = [10, 20, 50, 60, 100]
print(f"Lista original: {lista_numeros}")

lista_numeros[2] = 99
print(f"Lista modificada: {lista_numeros}")

#EJERCICIO C
lista = [10, 20, 30, 40, 50, 60, 70]
print(f"Los primeros 3 elementos de la lista: {lista[:4]}")
print(f"Los ultimos 2 elementos de la lista: {lista[-2:]}")
print(f"Elementos del indice 2 al 4: {lista[2:5]}")


#EJERCICIO D
lista_frutas = ["manzana", "banana", "pera"]
print(f"Lista original: {lista_frutas}")

lista_frutas.append("uva")
print(f"Lista con el nuevo string uva: {lista_frutas}")

#EJERCICIO E
numeros = [3, 6, 9, 12, 15]
suma = 0
for elementos in range(len(numeros)):
    suma += numeros[elementos]
    
print(f"La suma de todos los elementos de la lista es: {suma}")


#EJERCICIO F
matriz = [
    ["Joel", 30, 10.5], 
    ["Region", -30, -10.5]
]

print(f"{matriz[1][2]}, {matriz[0][0]}, {matriz[0][2]}")