from datetime import datetime

# Paso 2: Solicitar entrada al usuario
entrada = input("Escribe tu entrada para el diario:\n")

# Paso 3: Abrir el archivo en modo de adición
with open("diario.txt", "a", encoding="utf-8") as archivo:
    # Paso 4: Escribir fecha, hora y entrada
    fecha_hora = datetime.now()
    archivo.write(f"{fecha_hora.date()} {fecha_hora.strftime('%H:%M:%S')} - {entrada}\n")
    archivo.write("\n---------------------------------------------------------------------\n")  # Separador