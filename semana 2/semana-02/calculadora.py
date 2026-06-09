# Desafio Final - Script 1: Calculadora
# Pede 2 números e uma operação e mostra o resultado. Loop automático.

print("=== CALCULADORA PYTHON ===")

while True:
    print()

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("\nValor inválido! Digite apenas números.")
        continue

    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = numero1 + numero2
        print(f"\nResultado: {numero1} + {numero2} = {resultado}")

    elif operacao == "-":
        resultado = numero1 - numero2
        print(f"\nResultado: {numero1} - {numero2} = {resultado}")

    elif operacao == "*":
        resultado = numero1 * numero2
        print(f"\nResultado: {numero1} * {numero2} = {resultado}")

    elif operacao == "/":
        if numero2 == 0:
            print("\nErro: não é possível dividir por zero!")
        else:
            resultado = numero1 / numero2
            print(f"\nResultado: {numero1} / {numero2} = {resultado:.2f}")

    else:
        print("\nOperação inválida! Use +, -, * ou /")

    print()
    continuar = input("Fazer outro cálculo? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nAté logo!")
        break
