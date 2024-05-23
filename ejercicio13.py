# Ejercicio 13: Verificación de Número PrimoEscribe un programa que determine si un número ingresado por el usuario es primo o no.
import math
def es_primo (número):
  if número <= 1:
    return False
  if número == 2:
    return True
  for i in range(2,int(math.sqrt(número)) + 1):
    if número % i == 0:
      return False
  return True
número = int(input("Ingrese un número:"))    
if es_primo(número):
  print(f"El número{número} es primo.")
else:
  print(f"El número {número} no es primo.")  