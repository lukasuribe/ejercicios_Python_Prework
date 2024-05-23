#Ejercicio 18: Contador de Palabras Ejercicios Introducción a Python: Enunciados 3 Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
oración = input("Ingresa una oración:")
palabras = oración.split()
numero_de_palabras = len(palabras)
print(f"La cantidad de palabras en la oración es : {numero_de_palabras}")