# Projeto 4: Gerador de Senhas
# Usuário escolhe tamanho, maiúsculas, números e símbolos. Loop automático.

import random
import string

MINUSCULAS = string.ascii_lowercase
MAIUSCULAS = string.ascii_uppercase
NUMEROS = string.digits
SIMBOLOS = "!@#$%&*()_+-=[]{}?"


def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    caracteres = MINUSCULAS

    obrigatorios = []

    if usar_maiusculas:
        caracteres += MAIUSCULAS
        obrigatorios.append(random.choice(MAIUSCULAS))

    if usar_numeros:
        caracteres += NUMEROS
        obrigatorios.append(random.choice(NUMEROS))

    if usar_simbolos:
        caracteres += SIMBOLOS
        obrigatorios.append(random.choice(SIMBOLOS))

    restante = tamanho - len(obrigatorios)
    senha = obrigatorios + [random.choice(caracteres) for _ in range(restante)]

    random.shuffle(senha)
    return "".join(senha)


def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Digite 's' para sim ou 'n' para não.")


print("=== GERADOR DE SENHAS ===")

while True:
    print()

    while True:
        tamanho_input = input("Tamanho da senha (mínimo 6): ").strip()
        if tamanho_input.isdigit() and int(tamanho_input) >= 6:
            tamanho = int(tamanho_input)
            break
        print("Digite um número válido, mínimo 6.")

    usar_maiusculas = perguntar_sim_nao("Incluir letras maiúsculas? (s/n): ")
    usar_numeros    = perguntar_sim_nao("Incluir números? (s/n): ")
    usar_simbolos   = perguntar_sim_nao("Incluir símbolos (!@#...)? (s/n): ")

    senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)

    print(f"\nSenha gerada:  {senha}")
    print(f"Tamanho:       {len(senha)} caracteres")
    print("Guarde em um lugar seguro!")

    print()
    continuar = input("Gerar outra senha? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nAté logo!")
        break
