import pwinput
import os
import textwrap
from datetime import datetime

# Cargar usuarios del archivo usuarios.txt
def cargar_usuario():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, contraseña = linea.strip().split(",")
                usuarios[usuario] = contraseña
    return usuarios

# Verifica usuario y contraseña con 3 intentos
def inicio(usuarios):
    print(textwrap.dedent("""
    SISTEMA DE CAJAS INQUIDSA
    """))

    intentos = 0 
    while intentos < 3:
        usuario = input("Usuario: ")
        contraseña = pwinput.pwinput("Contraseña: ")

        if usuario in usuarios and usuarios[usuario] == contraseña:
            print(f"\nIniciando sesión...\nBienvenid@ {usuario}")
            return usuario
        else:
            print("\nUsuario o contraseña incorrectos.")
            intentos += 1

    print("\nLímite de intentos sobrepasado.")
    exit()

# Permite ingresar productos usando códigos desde el archivo categorias.txt
def ingreso_productos():
    productos = {}
    categoria_actual = ""

    with open("categorias.txt", "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea.startswith("[") and linea.endswith("]"):
                categoria_actual = linea[1:-1]
            elif linea:
                codigo, nombre, precio = linea.split(",")
                productos[codigo] = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "categoria": categoria_actual
                }

    print("\nProductos disponibles por código:")
    for cod, datos in productos.items():
        print(f"{cod} - {datos['nombre']} (${datos['precio']:.2f}) [{datos['categoria']}]")

    orden = []

    while True:
        codigo = input("\nIngrese el código del producto (o 'fin' para terminar): ").strip()
        if codigo.lower() == "fin":
            break
        if codigo in productos:
            try:
                cantidad = int(input("Cantidad: "))
                nombre = productos[codigo]["nombre"]
                precio = productos[codigo]["precio"]
                orden.append((nombre, precio, cantidad))
                print(f"Añadido: {nombre} x{cantidad}")
            except ValueError:
                print("Cantidad inválida.")
        else:
            print("Código no encontrado.")
    return orden

# Permite modificar la cantidad de un producto ya ingresado
def editar_orden(orden):
    if not orden:
        print("No hay productos en la orden actual.")
        return

    print("\nProductos en la orden:")
    for i, (nombre, precio, cantidad) in enumerate(orden, 1):
        print(f"{i}. {nombre} x{cantidad} (${precio:.2f} c/u)")

    try:
        posicion = int(input("Ingrese el número del producto que desea editar: "))
        if 1 <= posicion <= len(orden):
            nuevo_valor = int(input("Nueva cantidad: "))
            if nuevo_valor <= 0:
                print("La cantidad debe ser mayor que cero.")
            else:
                nombre, precio, _ = orden[posicion - 1]
                orden[posicion - 1] = (nombre, precio, nuevo_valor)
                print(f"Producto '{nombre}' actualizado con nueva cantidad: {nuevo_valor}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada no válida.")

# Elimina toda la orden actual del cliente
def eliminar_orden(orden):
    confirmacion = input("¿Seguro que deseas eliminar toda la orden? (s/n): ").strip().lower()
    if confirmacion == "s":
        orden.clear()
        print("Orden eliminada correctamente.")
    else:
        print("Eliminación cancelada.")

# Calcula el total de la orden sumando todos los productos
def cuenta(productos):
    total = sum(precio * cantidad for _, precio, cantidad in productos)
    return total

# Genera un archivo factura.txt y guarda el total en registro_facturas.txt
def imprimir_factura(productos, total, usuario):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("factura.txt", "w",encoding = "utf-8") as f:
        f.write("FACTURA\n")
        f.write(f"Cajero: {usuario}\n")
        f.write(f"Fecha y hora: {now}\n\n")
        for nombre, precio, cantidad in productos:
            subtotal = precio * cantidad
            f.write(f"{nombre} x{cantidad} = ${subtotal:.2f}\n")
        f.write(f"\nTOTAL: ${total:.2f}\n")

    with open("registro_facturas.txt", "a") as r:
        r.write(f"{now} - Cajero: {usuario} - Total: ${total:.2f}\n")

    print("Factura generada con éxito.")

# Cierra el programa inmediatamente por emergencia
def cerrado_urgente():
    print("EMERGENCIA: Caja cerrada por seguridad.")
    exit()

# Registra el dinero total acumulado en el archivo registro_dinero.py
def registrar_dinero(monto):
    archivo = "registro_dinero.py"

    if not os.path.exists(archivo):
        with open(archivo, "w") as f:
            f.write("dinero_total = 0")

    contexto = {}
    with open(archivo, "r") as f:
        exec(f.read(), contexto)

    total_actual = contexto.get("dinero_total", 0)
    total_actual += monto

    with open(archivo, "w") as f:
        f.write(f"dinero_total = {total_actual}")
