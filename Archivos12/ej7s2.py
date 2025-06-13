#Solicitamos datos al usuario
nombre= input("Introduce tu nombre: ")
apellido= input("Introduce tu apellido: ")
edad= input("Introduce tu edad: ")
salario= input("Introduce tu salario: ")

#formatear los datos de una linea
linea = f"{nombre} {apellido} {edad} {salario}\n"

#guardar los datos en un archivo
with open("datos.txt", "a") as archi1:  # Abrir el archivo en modo append
    archi1.write(linea)  # Escribir la línea en el archivo

# Imprimir mensaje de finalización
print("\nDatos guardados correctamente en el archivo 'datos.txt'.")  # Añadir un salto de línea antes del mensaje final