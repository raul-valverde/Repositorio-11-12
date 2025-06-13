archi1=open("datos.txt", "r+")
# Ejemplo de lectura y escritura en un archivo con modo "r+"
# Leer el contenido del archivo
contenido = archi1.read()
# Imprimir el contenido del archivo 
print(contenido)
# agregar más contenido al archivo
archi1.write("Nueva línea añadida al final del archivo.\n")
archi1.write("Otra línea añadida al final del archivo.\n")
# Cerrar el archivo
archi1.close()
# Imprimir mensaje de finalización
print("Final del programa")
# Nota: El modo "r+" permite leer y escribir en el archivo,
# pero no permite truncar el archivo. Si se desea truncar, se debe usar "w+" o "a+".