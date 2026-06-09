# Projeto 4: Gerador de Senhas
# Gera 5 senhas de uma vez, salva em senhas.txt com data. Loop automático.

import random
import string
from datetime import datetime

MINUSCULAS = string.ascii_lowercase
MAIUSCULAS = string.ascii_uppercase
NUMEROS = string.digits
SIMBOLOS = "!@#$%&*()_+-=[]{}?"
QUANTIDADE = 5


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


def salvar_senhas(senhas, tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    tipos = []
    if usar_maiusculas:
        tipos.append("Maiúsculas")
    if usar_numeros:
        tipos.append("Números")
    if usar_simbolos:
        tipos.append("Símbolos")
    tipos_str = ", ".join(tipos) if tipos else "Apenas minúsculas"

    with open("senhas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{'=' * 40}\n")
        arquivo.write(f"Data: {agora}\n")
        arquivo.write(f"Tamanho: {tamanho} | Tipos: {tipos_str}\n")
        arquivo.write(f"{'=' * 40}\n")
        for i, senha in enumerate(senhas, start=1):
            arquivo.write(f"{i}. {senha}\n")
        arquivo.write("\n")


print("=== GERADOR DE SENHAS ===")
print(f"Gera {QUANTIDADE} senhas por vez e salva em senhas.txt")

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

    senhas = [gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
              for _ in range(QUANTIDADE)]

    print(f"\n--- {QUANTIDADE} senhas geradas ---")
    for i, senha in enumerate(senhas, start=1):
        print(f"  {i}. {senha}")

    salvar_senhas(senhas, tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
    print("\nSenhas salvas em 'senhas.txt' com data e hora!")

    print()
    continuar = input("Gerar mais senhas? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nAté logo!")
        break
