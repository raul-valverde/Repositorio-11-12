import csv

# Solicita al usuario el nombre del producto
producto_buscado = input("Introduce el nombre del producto: ").strip().lower()

total_ingresos = 0
total_unidades = 0

# Ruta del archivo en el mismo directorio
ruta_archivo = "ventas.csv"

try:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            # Quita espacios de cada campo
            producto = fila[0].strip().lower()
            cantidad = int(fila[1].strip())
            fecha = fila[2].strip()
            precio = float(fila[3].strip())
            if producto == producto_buscado:
                total_unidades += cantidad
                total_ingresos += cantidad * precio

    # Mostrar resultados
    print(f"\nProducto: {producto_buscado.title()}")
    print(f"Total de unidades vendidas: {total_unidades}")
    print(f"Ingresos generados: ${total_ingresos:.2f}")

except FileNotFoundError:
    print(f"No se encontró el archivo en la ruta: {ruta_archivo}")
except Exception as e:
    print(f"Ocurrió un error: {e}")