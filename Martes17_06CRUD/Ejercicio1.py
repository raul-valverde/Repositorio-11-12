#.- Lectura de un archivo de texto simple: Escribe un programa que lea un archivo de texto llamado “poema.txt” e imprima su contenido línea por línea.
def leer_poema():
    try:
        with open("poema.txt", "r", encoding="utf-8") as archivo:
            #Le asignamos el arhivo que va a leer
            for linea in archivo:
                print(linea.strip())
                #que lo imprima linea por linea
    except FileNotFoundError:
        #si el archivo no existe o no lo encuentra, se enviara un print con un mensaje de error
        print("El archivo 'poema.txt' no existe.")

leer_poema()
