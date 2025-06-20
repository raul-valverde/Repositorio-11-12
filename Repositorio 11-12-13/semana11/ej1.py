"""	Crear un programa que dado un monto para presupuesto anual de una fábrica calcule el porcentaje de dinero que le corresponde a cada departamento. El cálculo se realizará en una función que recibe como argumento el monto.
Recursos Humanos		50%
Manufactura			25%
Empaquetado		15%
Publicidad			10"""

def calcular_presupuesto_anual(monto):
    """Calcula el presupuesto anual para cada departamento basado en el monto total."""
    presupuesto = {
        "Recursos Humanos": monto * 0.50,
        "Manufactura": monto * 0.25,
        "Empaquetado": monto * 0.15,
        "Publicidad": monto * 0.10
    }
    return presupuesto

# Solicitar el monto al usuario
monto = float(input("Ingrese el monto del presupuesto anual: "))
presupuesto = calcular_presupuesto_anual(monto)

print("\nDistribución del presupuesto:")
for departamento, cantidad in presupuesto.items():
    print(f"{departamento}: ${cantidad:.2f}")