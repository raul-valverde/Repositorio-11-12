def calcular_descuento_renta(salario):
    """Calcula el descuento de renta del 10% sobre el salario."""
    return salario * 0.10

n = int(input("Ingrese la cantidad de empleados: "))

for i in range(1, n + 1):
    print(f"\nEmpleado {i}:")
    salario = float(input("  Ingrese el salario: "))
    descuento = calcular_descuento_renta(salario)
    total_pagar = salario - descuento
    print(f"  Descuento de renta: ${descuento:.2f}")
    print(f"  Total a pagar: ${total_pagar:.2f}")