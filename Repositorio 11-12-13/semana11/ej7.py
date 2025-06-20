def menor_de_tres(a, b, c):
    """Devuelve el menor de tres números reales."""
    return min(a, b, c)

x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
z = float(input("Ingrese el tercer número: "))

menor = menor_de_tres(x, y, z)
print(f"El menor de los tres números es: {menor}")