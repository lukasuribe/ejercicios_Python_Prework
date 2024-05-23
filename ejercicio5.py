#Ejercicio 5: Suma de Números Pares Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
suma = 0
for número in range(1, 100):
  if número % 2== 0:
    suma += número
print(f"La suma de los números pares del 1 hasta el 100 es: {suma}")