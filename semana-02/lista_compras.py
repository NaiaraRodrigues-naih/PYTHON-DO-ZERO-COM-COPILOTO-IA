# Projeto 2: Lista de Compras
# Menu com opções: adicionar, ver, remover item e sair

lista = []

print("=== LISTA DE COMPRAS ===")

while True:
    print()
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Remover item")
    print("0 - Sair")
    print()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)
        print(f'"{item}" adicionado à lista!')

    elif opcao == "2":
        if len(lista) == 0:
            print("\nA lista está vazia!")
        else:
            print("\n--- Sua lista de compras ---")
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")
            print(f"\nTotal: {len(lista)} item(s)")

    elif opcao == "3":
        if len(lista) == 0:
            print("\nA lista está vazia, nada para remover!")
        else:
            print("\n--- Sua lista de compras ---")
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")
            print()
            numero = input("Digite o número do item a remover: ")
            if numero.isdigit() and 1 <= int(numero) <= len(lista):
                removido = lista.pop(int(numero) - 1)
                print(f'"{removido}" removido da lista!')
            else:
                print("Número inválido!")

    elif opcao == "0":
        if len(lista) > 0:
            with open("lista_compras.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("=== LISTA DE COMPRAS ===\n\n")
                for i, item in enumerate(lista, start=1):
                    arquivo.write(f"{i}. {item}\n")
                arquivo.write(f"\nTotal: {len(lista)} item(s)\n")
            print("\nLista salva em 'lista_compras.txt'!")
        print("\nAté logo!")
        break

    else:
        print("\nOpção inválida. Digite 1, 2, 3 ou 0.")
