# Desafio Final - Script 2: Lista de Compras
# Permite adicionar itens e mostra a lista final

print("=== LISTA DE COMPRAS ===")

lista = []

while True:
    item = input("Digite um item (ou 'sair' para encerrar): ")

    if item.lower() == "sair":
        break

    lista.append(item)
    print("Item '" + item + "' adicionado!")

print("\n--- Sua lista de compras ---")

if len(lista) == 0:
    print("A lista esta vazia!")
else:
    for i in range(len(lista)):
        print(str(i + 1) + ". " + lista[i])

print("\nTotal de itens: " + str(len(lista)))
