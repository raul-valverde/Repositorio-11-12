# Ejercicio 4: Leer un archivo CSV y mostrar los datos ordenados
with open("productos.csv", "r", encoding="utf-8") as archivo:
    # Paso 2: Recorrer el archivo línea por línea
    for linea in archivo:
        # Paso 3: Eliminar salto de línea
        linea = linea.strip()
        # Paso 4: Separar en nombre, precio y cantidad
        partes = linea.split(',')
        if len(partes) == 3:
             nombre, precio, cantidad = partes
            # Paso 5: Imprimir datos ordenados
             print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")
