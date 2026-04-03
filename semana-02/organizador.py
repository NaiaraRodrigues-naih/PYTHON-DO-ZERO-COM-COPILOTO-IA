# Desafio Final - Script 5: Organizador de Nomes
# Recebe uma lista de nomes e organiza em ordem alfabetica

print("=== ORGANIZADOR DE NOMES ===")

nomes = []

print("Digite os nomes um por um. Quando terminar, digite 'sair'.\n")

while True:
    nome = input("Digite um nome: ").strip()

    if nome.lower() == "sair":
        break

    if nome != "":
        nomes.append(nome)
        print("Nome '" + nome + "' adicionado!")

if len(nomes) == 0:
    print("\nNenhum nome foi digitado!")
else:
    print("\n--- Nomes antes de organizar ---")
    for nome in nomes:
        print("- " + nome)

    nomes.sort()

    print("\n--- Nomes em ordem alfabetica ---")
    for i in range(len(nomes)):
        print(str(i + 1) + ". " + nomes[i])

    print("\nTotal: " + str(len(nomes)) + " nomes organizados!")
