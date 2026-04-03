# Desafio Final - Script 4: Gerador de Senhas
# Gera senhas aleatorias com tamanho escolhido pelo usuario

import random

print("=== GERADOR DE SENHAS ===")

letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*"

todos_caracteres = letras_minusculas + letras_maiusculas + numeros + simbolos

tamanho = int(input("Qual o tamanho da senha? (minimo 6): "))

if tamanho < 6:
    print("Tamanho muito pequeno! Usando 6 como minimo.")
    tamanho = 6

senha = ""
for i in range(tamanho):
    caractere = random.choice(todos_caracteres)
    senha += caractere

print("\nSua senha gerada: " + senha)
print("Tamanho: " + str(len(senha)) + " caracteres")
print("\nGuarde sua senha em um lugar seguro!")
