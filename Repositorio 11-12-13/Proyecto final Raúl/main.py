from funciones import cargar_usuario,inicio,editar_orden,eliminar_orden,imprimir_factura,cuenta,cerrado_urgente,ingreso_productos,registrar_dinero

def main():
    usuarios = cargar_usuario()
    usuario = inicio(usuarios)

    orden = []

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Ingresar productos")
        print("2. Editar orden")
        print("3. Eliminar orden")
        print("4. Imprimir factura")
        print("5. Cierre de emergencia")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            orden += ingreso_productos()
        elif opcion == "2":
            editar_orden(orden)
        elif opcion == "3":
            eliminar_orden(orden)
        elif opcion == "4":
            if orden:
                total = cuenta(orden)
                imprimir_factura(orden, total, usuario)
                registrar_dinero(total)
                orden.clear()  # reinicia orden para siguiente cliente
            else:
                print("No hay productos para facturar.")
        elif opcion == "5":
            cerrado_urgente()
        elif opcion == "6":
            print("\nCerrando caja. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida.")

main()