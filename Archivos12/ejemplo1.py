#Ejemplificando archivos
#Declarar un objet de tipo archivo
archi1 = open("datos.txt", "w")
archi1.write("Hola, mundo!\n")
archi1.write("Este es un ejemplo de archivo en Python.\n")
archi1.write("Adis, mundo!\n")
archi1.write("Segunda linea\n")
#Agregar más contenido al archivo
archi1 = open("datos.txt", "a")
archi1.write("cuarta\n")
archi1.write("Quinta\n")
archi1.write("SEXTA!\n")
#Cerrar el archivo
archi1.close()
print("Final del programa")
