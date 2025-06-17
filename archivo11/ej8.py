def calcular_importe_final(importe):
    """Devuelve el importe final aplicando el descuento correspondiente."""
    if importe > 800:
        descuento = 0.12
    elif importe > 500:
        descuento = 0.10
    elif importe > 300:
        descuento = 0.05
    else:
        descuento = 0.0
    return importe * (1 - descuento)

importe = float(input("Ingrese el importe de la compra (€): "))
final = calcular_importe_final(importe)
print(f"El importe final a pagar" f" es: €{final:.2f}")

"""Lo altere un poco para que no sea a como dice la orientacion ya que
no me gusta que tenga que elegir entre 2  500€ (del 10% cuando se compra más de 500 €
 y del 12% para cantidades mayores de 500 €, ) y pues por eso puse qeu era un 12% para
 los importes mayores a 800€ y un 10% para los mayores a 500€ y un 5% para los mayores a 300€
y un 0% para los menores a 300€"""
