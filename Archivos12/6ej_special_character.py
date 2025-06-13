#Leer caracteres especiales en un archivo de texto
# Crear un archivo de texto con caracteres especiales
archi1 = open("datos.txt", "w", encoding="utf-8")
archi1.write("¡Hola, mundo!\n")
archi1.write("Este es un ejemplo de archivo con caracteres especiales: ñ, á, é, í, ó, ú.\n")
archi1.write("Adiós, mundo!\n")
# Cerrar el archivo
archi1.close()

# Leer el archivo con caracteres especiales
archi1 = open("datos.txt", "r", encoding="utf-8")
lineas = archi1.readlines()  # Leer todas las líneas del archivo
print("Contenido del archivo con caracteres especiales:")
for linea in lineas:
    print(linea, end='')  # Imprimir cada línea sin agregar una nueva línea extra
archi1.close()  # Cerrar el archivo
# Imprimir mensaje de finalización
print("\nFinal del programa")  # Añadir un salto de línea antes del mensaje final