# Ejercicio 20: Suma de Números en una Lista Crea un programa que sume todos los números en una lista ingresada por el usuario.
lista_numeros = input("Ingresa una lista de números separados por comas:")
números = [int(num) for num in lista_numeros.split(',')]
suma_total = 0
for num in números:
    suma_total += num
print(f"La suma de los númeroes de la lista es : {suma_total}")