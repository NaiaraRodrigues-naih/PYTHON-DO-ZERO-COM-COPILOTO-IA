# Projeto 1: Calculadora Conversora
# Converte temperaturas entre Celsius e Fahrenheit

print("=== CALCULADORA CONVERSORA DE TEMPERATURA ===")

while True:
    print()
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("0 - Sair")
    print()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"\nResultado: {celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            print("\nValor inválido! Digite apenas números.")

    elif opcao == "2":
        try:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"\nResultado: {fahrenheit}°F = {celsius:.2f}°C")
        except ValueError:
            print("\nValor inválido! Digite apenas números.")

    elif opcao == "0":
        print("\nAté logo!")
        break

    else:
        print("\nOpção inválida. Digite 1, 2 ou 0.")
