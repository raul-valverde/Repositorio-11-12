def calcular_pago(horas):
    """Calcula el pago según las horas trabajadas."""
    if horas <= 160:
        return horas * 6.5
    else:
        extras = horas - 160
        return (160 * 6.5) + (extras * 7.5)

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
pago = calcular_pago(horas_trabajadas)
print(f"El valor a pagar es: ${pago:.2f}")