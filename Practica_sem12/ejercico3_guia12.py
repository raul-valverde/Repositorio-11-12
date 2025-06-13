# Paso 1: Abrir el archivo en modo escritura para iniciar una nueva lista
with open("compras.txt", "w", encoding="utf-8") as archivo:
    # Paso 2: Bucle infinito
    while True:
        # Paso 3: Pedir producto al usuario
        producto = input("Ingresa un producto (o escribe 'fin' para terminar): ")
        # Paso 4: Comprobar si es 'fin'
        if producto.lower() == "fin":
            break
        # Paso 5: Escribir producto en el archivo
        archivo.write(producto + "\n")

# Paso 6: Notificar al usuario
print("¡Lista de compras guardada en el archivo 'compras.txt'!")