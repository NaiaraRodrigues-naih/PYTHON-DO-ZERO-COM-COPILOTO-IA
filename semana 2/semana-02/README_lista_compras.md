# Projeto 2: Lista de Compras

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Programa de lista de compras com menu interativo. O usuário pode **adicionar**, **ver** e **remover** itens, e o programa fica rodando em loop até o usuário escolher sair.

---

## Como usar

1. Execute o script no terminal:
   ```bash
   python lista_compras.py
   ```

2. Escolha uma opção no menu:
   ```
   === LISTA DE COMPRAS ===

   1 - Adicionar item
   2 - Ver lista
   3 - Remover item
   0 - Sair
   ```

3. Exemplo de uso completo:
   ```
   Escolha uma opção: 1
   Digite o item: Arroz
   "Arroz" adicionado à lista!

   Escolha uma opção: 1
   Digite o item: Feijão
   "Feijão" adicionado à lista!

   Escolha uma opção: 2

   --- Sua lista de compras ---
   1. Arroz
   2. Feijão

   Total: 2 item(s)

   Escolha uma opção: 3

   --- Sua lista de compras ---
   1. Arroz
   2. Feijão

   Digite o número do item a remover: 1
   "Arroz" removido da lista!

   Escolha uma opção: 0

   Até logo!
   ```

---

## Explicação do código

### 1. Lista vazia para guardar os itens
```python
lista = []
```
Cria uma lista vazia. Todos os itens adicionados serão guardados aqui durante a execução do programa.

---

### 2. Loop automático com while
```python
while True:
    ...
```
Mantém o programa rodando indefinidamente. Só para quando o usuário digita `0` e o `break` é executado.

---

### 3. Adicionar item (opção 1)
```python
item = input("Digite o item: ")
lista.append(item)
print(f'"{item}" adicionado à lista!')
```
- `input()` captura o item digitado
- `.append()` adiciona o item ao final da lista
- f-string exibe a confirmação com o nome do item

---

### 4. Ver lista (opção 2)
```python
for i, item in enumerate(lista, start=1):
    print(f"{i}. {item}")
print(f"\nTotal: {len(lista)} item(s)")
```
- `enumerate()` percorre a lista retornando o número e o item ao mesmo tempo
- `start=1` faz a contagem começar em 1 (não em 0)
- `len()` conta o total de itens

---

### 5. Remover item (opção 3)
```python
numero = input("Digite o número do item a remover: ")
if numero.isdigit() and 1 <= int(numero) <= len(lista):
    removido = lista.pop(int(numero) - 1)
    print(f'"{removido}" removido da lista!')
```
- `isdigit()` verifica se o usuário digitou um número válido
- A condição garante que o número está dentro do tamanho da lista
- `.pop()` remove o item pelo índice e retorna o valor removido
- `int(numero) - 1` converte para índice (a lista começa em 0, o menu em 1)

---

### 6. Sair (opção 0)
```python
elif opcao == "0":
    print("\nAté logo!")
    break
```
`break` encerra o `while True`, finalizando o programa.

---

## Conceitos Python utilizados

| Conceito | Uso no projeto |
|---|---|
| `list` | Armazena os itens da lista de compras |
| `.append()` | Adiciona item ao final da lista |
| `.pop()` | Remove item pelo índice |
| `len()` | Conta o total de itens |
| `enumerate()` | Percorre lista com número e valor ao mesmo tempo |
| `while True` | Loop automático que mantém o programa rodando |
| `break` | Encerra o loop quando o usuário sai |
| `isdigit()` | Valida se a entrada é um número |
| `if / elif / else` | Controla as opções do menu |
| f-string (`f"..."`) | Formata as mensagens de saída |

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
