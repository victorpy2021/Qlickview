def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

operacion = input("¿Quieres sumar o restar? (Escribe 'sumar' o 'restar'): ")

if operacion == 'sumar':
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = sumar(num1, num2)
    print("El resultado de la suma es:", resultado)
elif operacion == 'restar':
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = restar(num1, num2)
    print("El resultado de la resta es:", resultado)
else:
    print("Operación no válida. Por favor, selecciona 'sumar' o 'resstar'.")
