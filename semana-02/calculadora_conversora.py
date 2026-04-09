# Projeto 1: Calculadora Conversora
# Converte Celsius para Fahrenheit

print("=== CALCULADORA CONVERSORA DE TEMPERATURA ===")
print()

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print()
print(f"Resultado: {celsius}°C = {fahrenheit:.2f}°F")
