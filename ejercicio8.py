# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC) Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {imc: .2f}")