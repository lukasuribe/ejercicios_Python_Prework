# Ejercicio 11: Calculadora de Edad Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
from datetime import datetime
año_de_nacimiento = int(input("Escriba su año de nacimiento:"))
año_actual = datetime.now().year
edad = año_actual - año_de_nacimiento
print(f"Tienes {edad} años.")