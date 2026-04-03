# Desafio Final - Script 3: Quiz
# 5 perguntas sobre Python e tecnologia. Conta os acertos no final!

print("=== QUIZ: PYTHON E TECNOLOGIA ===")
print("Responda as perguntas abaixo!\n")

acertos = 0

# Pergunta 1
resposta1 = input("1. Qual comando usamos para exibir algo na tela em Python? ").strip().lower()
if resposta1 == "print":
    print("Correto!\n")
    acertos += 1
else:
    print("Errado! A resposta era: print\n")

# Pergunta 2
resposta2 = input("2. Como chamamos uma variavel que guarda Verdadeiro ou Falso? ").strip().lower()
if resposta2 == "booleano" or resposta2 == "bool":
    print("Correto!\n")
    acertos += 1
else:
    print("Errado! A resposta era: booleano (bool)\n")

# Pergunta 3
resposta3 = input("3. Qual simbolo usamos para fazer comentarios em Python? ").strip()
if resposta3 == "#":
    print("Correto!\n")
    acertos += 1
else:
    print("Errado! A resposta era: #\n")

# Pergunta 4
resposta4 = input("4. Como criamos uma funcao em Python? (palavra-chave) ").strip().lower()
if resposta4 == "def":
    print("Correto!\n")
    acertos += 1
else:
    print("Errado! A resposta era: def\n")

# Pergunta 5
resposta5 = input("5. Qual funcao converte um numero em texto em Python? ").strip().lower()
if resposta5 == "str" or resposta5 == "str()":
    print("Correto!\n")
    acertos += 1
else:
    print("Errado! A resposta era: str()\n")

# Resultado final
print("=== RESULTADO FINAL ===")
print("Voce acertou " + str(acertos) + " de 5 perguntas!")

if acertos == 5:
    print("Perfeito! Voce e uma futura dev incrivel!")
elif acertos >= 3:
    print("Muito bem! Continue praticando!")
else:
    print("Continue estudando, voce vai chegar la!")
