#Leer el contenido del archivo "datos.txt" línea por línea con WHILE

# Crear la variable para el archivo 
archi1 = open("datos.txt", "r")
# Leer el contenido del archivo línea por línea
linea=archi1.readline()
while linea != "":
    # Imprimir la línea leída
    print(linea, end='')  # end='' evita agregar una nueva línea extra
    # Leer la siguiente línea
    linea = archi1.readline()
archi1.close()  # Cerrar el archivo
# Imprimir mensaje de finalización  
print("\nFinal del programa")  # Añadir un salto de línea antes del mensaje final
# Nota: Se usa end='' en print para evitar agregar una nueva línea extra,
# ya que readline() ya incluye el salto de línea al final de cada línea leída.


#Leer el contenido del archivo "datos.txt" línea por línea con un bucle FOR
# Crear la variable para el archivo
archi2 = open("datos.txt", "r")
# Leer el contenido del archivo línea por línea con un bucle for    
for linea in archi2:
    # Imprimir la línea leída
    print(linea, end='')  # end='' evita agregar una nueva línea extra
archi2.close()  # Cerrar el archivo
# Imprimir mensaje de finalización
print("\nFinal del programa")  # Añadir un salto de línea antes del mensaje final
# ya que el bucle for ya maneja los saltos de línea al iterar sobre las líneas del archivo.