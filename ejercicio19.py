# Ejercicio 19: Verificación de Año Bisiesto Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no
año = int(input("Ingresa un año:"))
if (año % 4== 0 and año % 100 != 0) or (año % 400 == 0):
  es_bisiesto = True
else:
  es_bisiesto = False
if es_bisiesto:
   print(f"El año {año} es bisiesto.")
else:
   print(f"El año {año} no es bisiesto.")