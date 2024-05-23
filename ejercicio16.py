# Ejercicio 16: Contador de Números Pares e Impares Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario
lista_numeros = input("Ingresa una lista de numeros separados por comas:")
numeros = [int(num) for num in lista_numeros.split(',')]
contador_pares = 0
contador_immpares = 0
for num in numeros:
  if num % 2 == 0:
    contador_pares += 1
  else:
    contador_immpares += 1
print(f"Cantidad de número pares: {contador_pares}")
print(f"Cantidad de números impares: {contador_immpares}")
  