#Eliminar lineas del archivo
#Abrir el archivo y leer las lineas
with open("datos.txt", "r", encoding="utf-8", errors="replace") as archivo:
    lineas = archivo.readlines()

# Filtrar las líneas que no contienen "Segunda linea"
lineas_filtradas = [linea for linea in lineas if linea.strip() != "Segunda linea"]
#Sobreescribir el archivo con las líneas filtradas
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas_filtradas)

# Imprimir mensaje de finalización
print("\nLíneas eliminadas correctamente del archivo 'datos.txt'.")  # Añadir un salto de línea antes del mensaje final