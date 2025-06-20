#.- Lectura de un archivo de texto simple: Escribe un programa que lea un archivo de texto llamado “poema.txt” e imprima su contenido línea por línea.
def leer_poema():
    try:
        with open("poema.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("El archivo 'poema.txt' no existe.")

leer_poema()