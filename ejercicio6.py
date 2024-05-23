#Ejercicio 6: Verificación de Palíndromo Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
palabra = input("Escribe una palabra:")
palabra = palabra.lower()
if palabra == palabra[::-1]:
  print (f"La palabra '{palabra}' es un palíndromo.")
else:
  print(f"La palabra '{palabra}' no es un palíndromo.")