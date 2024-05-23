# Ejercicio 10: Determinar el Día de la Semana Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
número = int(input("Ingresa un número del 1 al 7 :"))
if número == 1:
   dia_semana = "Lunes"
elif número == 2:
   dia_semana = "Martes"
elif número == 3:
   dia_semana = "Miercoles"
elif número == 4:
   dia_semana = "Jueves"
elif número == 5:
   dia_semana = "Viernes"
elif número == 6:
   dia_semana = "Sabado"
elif número == 7:
   dia_semana = "Domingo"
if dia_semana: 
   print(f"El número {número} corresponde a {dia_semana}")