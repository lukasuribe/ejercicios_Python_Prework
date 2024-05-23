cantidad_dolares = float(input("Ingresa una cantidad de dolares:"))
tasa_cambio = 0.85
cantidad_euros = cantidad_dolares * tasa_cambio
print(f"{cantidad_dolares} dólares son {cantidad_euros:2f} euros.")