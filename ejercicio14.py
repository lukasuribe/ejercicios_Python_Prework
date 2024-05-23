# Ejercicio 14: Calculadora de Descuento Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%
precio_normal = float(input("Ingresa el precio normal del producto:"))
descuento = 0.20
precio_final = precio_normal * (1 - descuento)
print(f"El precio final con descuento del 20% es: {precio_final:.2f} euros")