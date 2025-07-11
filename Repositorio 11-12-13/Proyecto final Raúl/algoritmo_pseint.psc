Proceso SistemaFacturacion
    Definir usuarios, usuario, orden[100], opcion, total, n Como Entero
    n <- 0
    usuarios <- cargar_usuario()
    usuario <- inicio(usuarios)

    Repetir
        Escribir "\nMENÚ PRINCIPAL"
        Escribir "1. Ingresar productos"
        Escribir "2. Editar orden"
        Escribir "3. Eliminar orden"
        Escribir "4. Imprimir factura"
        Escribir "5. Cierre de emergencia"
        Escribir "6. Salir"
        Escribir "Seleccione una opción: "
        Leer opcion

        Segun opcion Hacer
            1:
                n <- ingreso_productos(orden, n)
            2:
                editar_orden(orden, n)
            3:
                eliminar_orden(orden, n)
            4:
                Si n > 0 Entonces
                    total <- cuenta(orden, n)
                    imprimir_factura(orden, total, usuario, n)
                    registrar_dinero(total)
                    n <- 0
                Sino
                    Escribir "No hay productos para facturar."
                FinSi
            5:
                cerrado_urgente()
            6:
                Escribir "\nCerrando caja. ¡Hasta pronto!"
                Salir
            De Otro Modo:
                Escribir "Opción inválida."
        FinSegun
    Hasta Que opcion = 6
FinProceso

// Nota: Las funciones como cargar_usuario, inicio, ingreso_productos, etc. deben ser implementadas como subprocesos o funciones en PSeInt según la lógica de tu sistema.
