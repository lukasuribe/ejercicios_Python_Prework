def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def mostrar_menu():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

mostrar_menu()

opcion = input("Elige una opción (1/2/3/4): ")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
if opcion == '1':
    print(f"La suma de {numero1} y {numero2} es: {suma(numero1, numero2)}")
elif opcion == '2':
    print(f"La resta de {numero1} y {numero2} es: {resta(numero1, numero2)}")
elif opcion == '3':
    print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion(numero1, numero2)}")
elif opcion == '4':
    resultado = division(numero1, numero2)
    if resultado == "Error: División por cero":
        print(resultado)
    else:
        print(f"La división de {numero1} y {numero2} es: {resultado}")
else:
    print("Opción no válida")
