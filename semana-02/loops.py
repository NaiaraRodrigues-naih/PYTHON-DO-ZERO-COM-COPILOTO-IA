# FOR  = para cada COR DE BLUSA FAÇA O SEGUINTE
cores_de_blusa = ["vermelha", "azul", "verde", "amarela", "preta"]
for cor in cores_de_blusa:
    print("Eu tenho uma blusa " + cor   + ".")
# WHILE = ENQUANTO A CONDIÇÃO FOR VERDADEIRA, FAÇA O SEGUINTE
contador = 0
while contador < 10:
    print("Contador: " + str(contador))
    contador += 1
# Exemplo de uso do while para contar de 1 a 10 e imprimir os números pares
contador = 1
while contador <= 10:
    if contador % 2 == 0:
        print("Número par: " + str(contador))
    contador += 1
    #while para contar de 1 a 10 e imprimir os números ímpares
contador = 1
while contador <= 10:
    if contador % 2 != 0:
        print("Número ímpar: " + str(contador))
    contador += 1
    #while para tabuada do 10   
contador = 1
while contador <= 10:
    resultado = 10 * contador
    print("10 x " + str(contador) + " = " + str(resultado))
    contador += 1
    #while para uma lista de nomes
nomes = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
contador = 0
while contador < len(nomes):
    print("Nome: " + nomes[contador])
    contador += 1
    
