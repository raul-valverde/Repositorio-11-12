#Ejercicio 7, crear un archivo con nombres de estudiantes y sus calificaciones separadas por coma, y escribimos un programa que calcules el promedio de las calificaciones de cada estudiante y lo guarde en un archivo llamado "promedios.txt". El archivo de entrada se llamará "estudiantes.csv" y tendrá el siguiente formato:
# nombre,calificacion1,calificacion2,calificacion3
def calcular_promedios():
    try:
        with open("estudiantes.csv", "r", encoding="utf-8") as archivo_entrada, \
             open("promedios.txt", "w", encoding="utf-8") as archivo_salida:
            for linea in archivo_entrada:
                partes = linea.strip().split(",")
                nombre = partes[0]
                try:
                    calificaciones = list(map(float, partes[1:]))
                    if calificaciones:
                        promedio = sum(calificaciones) / len(calificaciones)
                        archivo_salida.write(f"{nombre},{promedio:.2f}\n")
                except ValueError:
                    archivo_salida.write(f"{nombre},Error en calificaciones\n")
    except FileNotFoundError:
        print("El archivo 'notas.csv' no existe.")

calcular_promedios()