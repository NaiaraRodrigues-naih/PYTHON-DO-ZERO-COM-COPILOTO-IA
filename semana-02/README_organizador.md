# Desafio Final - Script 5: Organizador de Nomes

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Recebe uma lista de nomes digitados pelo usuário e os organiza em **ordem alfabética**. Mostra a lista antes e depois de ordenar. Roda em loop — o usuário pode organizar várias listas sem reiniciar o programa.

---

## Como usar

```bash
python organizador.py
```

Exemplo:
```
=== ORGANIZADOR DE NOMES ===

Digite os nomes um por um. Quando terminar, digite 'sair'.

Digite um nome: Zara
Nome 'Zara' adicionado!
Digite um nome: Ana
Nome 'Ana' adicionado!
Digite um nome: Carlos
Nome 'Carlos' adicionado!
Digite um nome: sair

--- Nomes antes de organizar ---
- Zara
- Ana
- Carlos

--- Nomes em ordem alfabética ---
1. Ana
2. Carlos
3. Zara

Total: 3 nomes organizados!

Organizar outra lista? (s/n): n

Até logo!
```

---

## Explicação do código

### 1. Loop externo — organizar outra lista
```python
while True:
    nomes = []
    ...
    continuar = input("Organizar outra lista? (s/n): ").strip().lower()
    if continuar != "s":
        break
```
A cada nova rodada, `nomes = []` zera a lista. O `break` sai quando o usuário digita `n`.

---

### 2. Loop interno — digitar os nomes
```python
while True:
    nome = input("Digite um nome: ").strip()
    if nome.lower() == "sair":
        break
    if nome != "":
        nomes.append(nome)
        print(f"Nome '{nome}' adicionado!")
```
Loop dedicado à entrada de nomes. `.strip()` remove espaços acidentais. A condição `nome != ""` evita adicionar entradas vazias.

---

### 3. Ordenação e exibição
```python
nomes.sort()

for i, nome in enumerate(nomes, start=1):
    print(f"{i}. {nome}")
```
- `.sort()` ordena a lista em ordem alfabética diretamente
- `enumerate()` com `start=1` numera a lista a partir de 1

---

## Conceitos Python utilizados

| Conceito | Uso |
|---|---|
| `list` + `.append()` | Armazena e adiciona nomes |
| `.sort()` | Ordena a lista alfabeticamente |
| `while True` aninhado | Loop externo (repetir) + loop interno (digitar) |
| `enumerate()` | Numera os nomes ao exibir |
| `.strip()` | Remove espaços extras da entrada |
| f-string | Formata as mensagens de saída |

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
