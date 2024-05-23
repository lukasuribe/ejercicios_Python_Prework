#Ejercicio 4: Contador de Vocales Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
palabra = (input("Ingresa una palabra:"))
contador_vocales = 0
vocales = "aeiouAEIOU"
for letra in palabra:
    if letra in vocales:
        contador_vocales += 1
print (f"El número de vocales en la palabra '{palabra}' es : {contador_vocales}")