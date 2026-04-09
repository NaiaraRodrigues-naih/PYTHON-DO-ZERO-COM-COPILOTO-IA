# Projeto 1: Calculadora Conversora
# Converte temperaturas entre Celsius e Fahrenheit

print("=== CALCULADORA CONVERSORA DE TEMPERATURA ===")
print()
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
print()

opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print()
    print(f"Resultado: {celsius}°C = {fahrenheit:.2f}°F")

elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print()
    print(f"Resultado: {fahrenheit}°F = {celsius:.2f}°C")

else:
    print("Opção inválida. Digite 1 ou 2.")
