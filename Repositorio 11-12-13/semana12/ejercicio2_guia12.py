# Paso 1: Solicitar el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo de texto (ej: poema.txt): ")

# Paso 2: Usar try...except para manejar FileNotFoundError
try:
    # Paso 3: Abrir el archivo en modo lectura
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        # Paso 4: Leer todas las líneas en una lista
        lineas = archivo.readlines()
        # Paso 5: Calcular y mostrar el número de líneas
        print(f"El archivo tiene {len(lineas)} líneas.")
except FileNotFoundError:
    # Paso 6: Mensaje de error amigable
    print("Error: El archivo no existe. Por favor, verifica el nombre e inténtalo de nuevo.")
# Paso 7: Mensaje de finalización
print("Operación completada.")