print("CALCULADORA BÁSICA")

num1 = float(input("Ingresa el primer número: "))
operador = input("Ingresa la operación (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))

if operador == "+":
    print("Resultado:", num1 + num2)
elif operador == "-":
    print("Resultado:", num1 - num2)
elif operador == "*":
    print("Resultado:", num1 * num2)
elif operador == "/":
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        print("Resultado:", num1 / num2)
else:
    print("Operación no válida.")