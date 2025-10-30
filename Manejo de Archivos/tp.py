import os

# Nombre del archivo para usar en todo el programa.
NOMBRE_ARCHIVO = "productos.txt"

# ----------------------------------------------------------------------
# 1. Crear el archivo inicial (función de configuración/inicialización)
# ----------------------------------------------------------------------
def inicializar_archivo(nombre_archivo):
    """Crea el archivo con datos iniciales si no existe,
    para asegurar que el programa funcione la primera vez."""
    
    # Usamos os.path.exists para verificar si el archivo ya fue creado antes
    if not os.path.exists(nombre_archivo):
        print(f"--- INICIALIZACIÓN: Creando '{nombre_archivo}' con datos de ejemplo.")
        
        datos_base = [
            "Lapicera,120.5,30",
            "Cuaderno,550.0,15",
            "Mochila,4500.99,5"
        ]
        
        # Usamos el modo 'w' (escritura) y 'with' para asegurar el cierre.
        try:
            with open(nombre_archivo, 'w') as f:
                for linea in datos_base:
                    f.write(linea + '\n')
            print("--- INICIALIZACIÓN: Archivo creado correctamente.")
        except IOError:
            print(f"ERROR: No se pudo crear el archivo {nombre_archivo}.")


# ----------------------------------------------------------------------
# 4. Cargar productos en una lista de diccionarios
# (Incluye el paso 2: leer y procesar)
# ----------------------------------------------------------------------
def cargar_productos_desde_archivo(nombre_archivo):
    """Abre el archivo, lee y procesa cada línea, y la guarda como
    un diccionario en una lista."""
    
    lista_productos = []
    
    try:
        # Abrimos en modo lectura 'r'
        with open(nombre_archivo, 'r') as f:
            print("\n--- PASO 4: Leyendo y cargando productos ---")
            for linea in f:
                # Paso 2: Procesar la línea
                # 1. Quitar espacios y saltos de línea (\n)
                linea_limpia = linea.strip()
                
                # 2. Separar por coma
                campos = linea_limpia.split(',')
                
                # Verificación simple de formato
                if len(campos) == 3:
                    try:
                        # Convertir a tipos de datos correctos
                        nombre = campos[0]
                        precio = float(campos[1])
                        cantidad = int(campos[2])
                        
                        # Crear el diccionario (Requisito 4)
                        producto = {
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        }
                        lista_productos.append(producto)
                        
                    except ValueError:
                        print(f"ADVERTENCIA: Saltando línea con error de tipo (precio/cantidad): {linea_limpia}")
                else:
                    print(f"ADVERTENCIA: Saltando línea con formato incorrecto (no 3 campos): {linea_limpia}")

    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{nombre_archivo}'. Asegúrese de que existe.")
    
    return lista_productos


# ----------------------------------------------------------------------
# 2. Mostrar productos (función auxiliar)
# ----------------------------------------------------------------------
def mostrar_productos(productos):
    """Muestra el contenido de la lista de diccionarios con el formato solicitado."""
    
    print("\n--- PASO 2: Productos cargados actualmente ---")
    if not productos:
        print("La lista está vacía.")
        return
        
    for p in productos:
        # Usamos f-string para formatear la salida (Requisito 2)
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")


# ----------------------------------------------------------------------
# 3. Agregar productos desde teclado
# ----------------------------------------------------------------------
def agregar_producto(productos):
    """Pide datos al usuario y añade un nuevo diccionario de producto a la lista."""
    
    print("\n--- PASO 3: Agregar Nuevo Producto ---")
    
    nombre_nuevo = input("Ingrese el nombre del nuevo producto: ").strip()
    
    # Pequeña validación de entrada
    if not nombre_nuevo:
        print("Adición cancelada. El nombre no puede estar vacío.")
        return

    while True:
        try:
            precio_nuevo = float(input(f"Ingrese el precio para {nombre_nuevo}: "))
            cantidad_nueva = int(input(f"Ingrese la cantidad para {nombre_nuevo}: "))
            
            if precio_nuevo < 0 or cantidad_nueva < 0:
                print("El precio y la cantidad deben ser positivos.")
                continue
            
            break # Salir del bucle si las entradas son válidas
        except ValueError:
            print("ERROR: Asegúrese de ingresar números válidos para precio y cantidad.")

    # Añadir el nuevo diccionario a la lista
    productos.append({
        "nombre": nombre_nuevo,
        "precio": precio_nuevo,
        "cantidad": cantidad_nueva
    })
    print(f"Producto '{nombre_nuevo}' agregado a la lista. (Pendiente de guardar en archivo)")


# ----------------------------------------------------------------------
# 5. Buscar producto por nombre
# ----------------------------------------------------------------------
def buscar_producto_por_nombre(productos):
    """Busca un producto por nombre en la lista y muestra sus detalles."""
    
    print("\n--- PASO 5: Buscar Producto ---")
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip()
    
    producto_encontrado = None
    
    # Recorrer la lista de diccionarios (Requisito 5)
    for p in productos:
        # Comparación insensible a mayúsculas/minúsculas para una mejor UX
        if p['nombre'].lower() == nombre_buscado.lower():
            producto_encontrado = p
            break # Detener la búsqueda si lo encuentra
            
    if producto_encontrado:
        print("\n¡Producto Encontrado!")
        print(f"Nombre: {producto_encontrado['nombre']}")
        print(f"Precio: ${producto_encontrado['precio']:.2f}")
        print(f"Cantidad: {producto_encontrado['cantidad']}")
    else:
        print(f"Producto NO ENCONTRADO: '{nombre_buscado}' no está en la lista.")


# ----------------------------------------------------------------------
# 6. Guardar los productos actualizados
# ----------------------------------------------------------------------
def guardar_productos_en_archivo(productos, nombre_archivo):
    """Sobrescribe el archivo con todos los productos de la lista (actualizados)."""
    
    print(f"\n--- PASO 6: Guardando {len(productos)} productos en '{nombre_archivo}' ---")
    
    try:
        # Abrimos en modo 'w' (escritura), lo que BORRA el contenido anterior.
        with open(nombre_archivo, 'w') as f:
            for p in productos:
                # Reconstruimos la línea en el formato nombre,precio,cantidad\n
                linea_a_escribir = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
                f.write(linea_a_escribir)
        print("--- PASO 6: Archivo actualizado y guardado con éxito.")
    except IOError:
        print(f"ERROR: No se pudo escribir en el archivo {nombre_archivo}.")


# ----------------------------------------------------------------------
# Función Principal (Main) para ejecutar el flujo completo
# ----------------------------------------------------------------------
def main():
    # Paso 1 (Configuración)
    inicializar_archivo(NOMBRE_ARCHIVO)
    
    # Pasos 4 y 2: Leer archivo y mostrar contenido inicial
    productos_actuales = cargar_productos_desde_archivo(NOMBRE_ARCHIVO)
    mostrar_productos(productos_actuales)

    # Paso 3: Agregar un producto
    agregar_producto(productos_actuales)
    
    # Paso 5: Buscar un producto
    buscar_producto_por_nombre(productos_actuales)
    
    # Paso 6: Guardar los cambios finales (incluye el producto agregado)
    guardar_productos_en_archivo(productos_actuales, NOMBRE_ARCHIVO)
    
    # Pequeña verificación final (opcional, pero útil para demostrar el guardado)
    print("\n*** Verificación: Volviendo a cargar el archivo para confirmar guardado. ***")
    productos_verificados = cargar_productos_desde_archivo(NOMBRE_ARCHIVO)
    mostrar_productos(productos_verificados)
    
    print("\n--- PROGRAMA FINALIZADO ---")

if __name__ == "__main__":
    main()