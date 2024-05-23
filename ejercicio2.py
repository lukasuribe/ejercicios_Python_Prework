#Ejercicio 2: Calculadora de PropinaCrea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
total_cuenta = float(input("Ingresa el total del consumo:"))
propina = total_cuenta * 0.15
monto_final = total_cuenta + propina
print(f"El total a pagar, incluyendo la propina, es: {monto_final}")