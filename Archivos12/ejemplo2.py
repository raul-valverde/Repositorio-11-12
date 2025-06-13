#Ejemplificar lectura de un archivo de texto
#Crear la variable para el archivo
archi2 = open("datos.txt", "r")
#Leer el contenido del archivo
contenido = archi2.read()
#Imprimir el contenido del archivo
print(contenido)        
#Cerrar el archivo
archi2.close()
#Imprimir mensaje de finalización
print("Final del programa")