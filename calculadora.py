# Desafio Final - Script 1: Calculadora
# Pede 2 numeros e uma operacao e mostra o resultado

print("=== CALCULADORA PYTHON ===")

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
operacao = input("Escolha a operacao (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado: " + str(numero1) + " + " + str(numero2) + " = " + str(resultado))

elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado: " + str(numero1) + " - " + str(numero2) + " = " + str(resultado))

elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado: " + str(numero1) + " * " + str(numero2) + " = " + str(resultado))

elif operacao == "/":
    if numero2 == 0:
        print("Erro: nao e possivel dividir por zero!")
    else:
        resultado = numero1 / numero2
        print("Resultado: " + str(numero1) + " / " + str(numero2) + " = " + str(resultado))

else:
    print("Operacao invalida! Use +, -, * ou /")
