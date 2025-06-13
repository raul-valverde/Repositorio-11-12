archi1=open("datos.txt", "r")  # Abrir el archivo en modo lectura
lineas=archi1.readlines()  # Leer todas las líneas del archivo
print("Contenido del archivo:", len(lineas), "líneas")
print("Contenido del archivo:")
for linea in lineas:
    print(linea, end='')  # Imprimir cada línea sin agregar una nueva línea extra
archi1.close()  # Cerrar el archivo
# Imprimir mensaje de finalización
print("\nFinal del programa")  # Añadir un salto de línea antes del mensaje final
