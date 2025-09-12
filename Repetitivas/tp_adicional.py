#1
print("**Palabra repetida**")
pedir_palabra = input("Ingresa una palabra: ")

for i in range(10):
    print(pedir_palabra)
    

#2
pedir_edad = int(input("Ingresa tu edad: "))

for i in range(1,pedir_edad):
    print(f"{i} años")

print(f"Edad actual: {pedir_edad} años")



#3
pedir_altura = int(input("Ingresa el valor limite para la altura del triangulo(con simbolos):"))
caracter = "*"
for i in range(1,pedir_altura+1):
    print(caracter)
    caracter += "*"
    

#4
producto = 0
num = int(input("Ingresa un numero para ver su tabla de multiplicar: "))
for i in range(1,11):
    producto = num*i
    print(f"{num} x {i} = {producto}")
    

#5
clave = "contraseña"
contador_intentos = 0
while True:
    pedir_clave = input("Ingresa tu contraseña: ")
    contador_intentos += 1
    if pedir_clave == clave:
        print("#Contraseña correcta#")
        break
    
    else:
        print("**Contraseña incorrecta**")
        

print(f"Has hecho {contador_intentos} intentos para tu clave.")

#6
while True:
    dato = input("Ingresa una palabra o un numero: ")
    if dato.capitalize() == "Salir":
        break
    else:
        print(dato)
    
    
#7
for i in range(2, 20 + 1):
    if i % 2 == 0:
        print(i)
    else:
        continue
    
#8
for i in range(1, 100 + 1):
    
    if i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    else:
        print(i)
        
#9
suma = 0
for i in range(1, 10 + 1):
    pedir_numero = int(input(f"Ingresa el n{i}: "))
    if i > 5:
        suma += pedir_numero
    else:
        continue
    
print(f"La suma de los ultimos 5 numeros ingresados es: {suma}")


#10
contador_equilatero = 0
contador_isosceles = 0
contador_escaleno = 0

while True:
    print("Clasificaion de los triangulos")
    
    print("Triangulo")
    lado_a = float(input("Ingresa el lado A: "))
    lado_b = float(input("Ingresa el lado B:"))
    lado_c = float(input("Ingresa el lado C: "))
    es_Triangulo = (lado_a + lado_b > lado_c) or (lado_a + lado_c > lado_b) or (lado_b + lado_c > lado_a)
    tipo_triangulo = ""
    if es_Triangulo:
        if (lado_a == lado_b) and (lado_a == lado_c):
            tipo_triangulo = "Equilatero"
            contador_equilatero += 1
        elif ((lado_a == lado_b) and (lado_c != lado_a or lado_c != lado_b)):
            tipo_triangulo = "Isosceles"
            contador_isosceles += 1
        else:
            tipo_triangulo = "Escaleno"
            contador_escaleno += 1
            
    print(f"Tipo De Triangulo: {tipo_triangulo}.")
    
    print("OPCIONES:")
    print("1.Agregar otro triangulo")
    print("2.salir")
    
    accion = int(input("Ingresa el numero de la opcion: "))
    if accion == 2:
        break

print(f"Cantidad de triangulos equilateros: {contador_equilatero}")
print(f"Cantidad de triangulos isosceles: {contador_isosceles}")
print(f"Cantidad de triangulos escaleno: {contador_escaleno}")