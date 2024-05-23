#Ejercicio 15: Conversor de Tiempo Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
cantidad_minutos = int(input("Ingresa una cantidad de minutos:"))
horas = cantidad_minutos // 60
minutos_restantes = cantidad_minutos % 60
print (f"{cantidad_minutos} son {horas} horas y {minutos_restantes} minutos.")

