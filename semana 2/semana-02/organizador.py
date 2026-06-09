# Desafio Final - Script 5: Organizador de Nomes
# Recebe uma lista de nomes e organiza em ordem alfabética. Loop automático.

print("=== ORGANIZADOR DE NOMES ===")

while True:
    nomes = []
    print("\nDigite os nomes um por um. Quando terminar, digite 'sair'.\n")

    while True:
        nome = input("Digite um nome: ").strip()
        if nome.lower() == "sair":
            break
        if nome != "":
            nomes.append(nome)
            print(f"Nome '{nome}' adicionado!")

    if len(nomes) == 0:
        print("\nNenhum nome foi digitado!")
    else:
        print("\n--- Nomes antes de organizar ---")
        for nome in nomes:
            print(f"- {nome}")

        nomes.sort()

        print("\n--- Nomes em ordem alfabética ---")
        for i, nome in enumerate(nomes, start=1):
            print(f"{i}. {nome}")

        print(f"\nTotal: {len(nomes)} nomes organizados!")

    print()
    continuar = input("Organizar outra lista? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nAté logo!")
        break
