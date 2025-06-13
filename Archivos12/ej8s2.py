#Trabajando con archivos de texto en Python
#1. Abrir el archivo en modo creacion
#Ejemplo, solicitando el nombre del archivo al usuario
ruta=input("Introduce el nombre del archivo: ")
archi1=open(ruta,"a")
#archi1.write("Primera linea ") y que salte de linea
#2. Escribir en el archivo
archi1.write("Primera linea\n")
#3. Agregar mas contenido al archivo
archi1.write("Segunda linea\n")
#4. Cerrar el archivo
archi1.close()
print("final del programa")