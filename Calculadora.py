import math


def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- CALCULADORA INTEGRADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")


def realizar_operacion(opcion, num1, num2=None):
    """Realiza el cálculo según la opción elegida."""
    if opcion == "1":
        return num1 + num2
    elif opcion == "2":
        return num1 - num2
    elif opcion == "3":
        return num1 * num2
    elif opcion == "4":
        if num2 == 0:
            return "Error: No se puede dividir entre cero."
        return num1 / num2
    elif opcion == "5":
        return num1**num2
    elif opcion == "6":
        if num1 < 0:
            return "Error: No se puede calcular la raíz de un número negativo."
        return math.sqrt(num1)
    else:
        return "Opción no válida."


def ejecutar_calculadora():
    """Controla el flujo principal del programa."""
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ")

    if opcion == "6":
        num1 = float(input("Ingresa el número: "))
        resultado = realizar_operacion(opcion, num1)
    elif opcion in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = realizar_operacion(opcion, num1, num2)
    else:
        resultado = "Opción no válida."

    print("Resultado:", resultado)


if __name__ == "__main__":
    ejecutar_calculadora()