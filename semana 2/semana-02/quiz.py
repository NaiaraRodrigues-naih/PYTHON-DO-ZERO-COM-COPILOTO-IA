# Desafio Final - Script 3: Quiz
# 5 perguntas sobre Python e tecnologia. Conta os acertos no final! Loop automático.

perguntas = [
    {"pergunta": "1. Qual comando usamos para exibir algo na tela em Python? ",
     "respostas": ["print"], "gabarito": "print"},
    {"pergunta": "2. Como chamamos uma variável que guarda Verdadeiro ou Falso? ",
     "respostas": ["booleano", "bool"], "gabarito": "booleano (bool)"},
    {"pergunta": "3. Qual símbolo usamos para fazer comentários em Python? ",
     "respostas": ["#"], "gabarito": "#"},
    {"pergunta": "4. Como criamos uma função em Python? (palavra-chave) ",
     "respostas": ["def"], "gabarito": "def"},
    {"pergunta": "5. Qual função converte um número em texto em Python? ",
     "respostas": ["str", "str()"], "gabarito": "str()"},
]

print("=== QUIZ: PYTHON E TECNOLOGIA ===")

while True:
    print("\nResponda as perguntas abaixo!\n")
    acertos = 0

    for q in perguntas:
        resposta = input(q["pergunta"]).strip().lower()
        if resposta in q["respostas"]:
            print("Correto!\n")
            acertos += 1
        else:
            print(f"Errado! A resposta era: {q['gabarito']}\n")

    print("=== RESULTADO FINAL ===")
    print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")

    if acertos == len(perguntas):
        print("Perfeito! Você é uma futura dev incrível!")
    elif acertos >= 3:
        print("Muito bem! Continue praticando!")
    else:
        print("Continue estudando, você vai chegar lá!")

    print()
    continuar = input("Jogar novamente? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nAté logo!")
        break
