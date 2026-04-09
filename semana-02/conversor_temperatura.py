# Projeto 1: Calculadora Conversora
# Converte Celsius para Fahrenheit

print("=== CONVERSOR DE TEMPERATURA ===")

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")