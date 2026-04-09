# Desafio Final - Script 3: Quiz Python e Tecnologia

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Quiz com **5 perguntas sobre Python e tecnologia**. O usuário digita a resposta livremente, o programa verifica, conta os acertos e exibe o placar ao final. Roda em loop — o usuário pode jogar várias vezes seguidas.

---

## Como usar

```bash
python quiz.py
```

Exemplo:
```
=== QUIZ: PYTHON E TECNOLOGIA ===

Responda as perguntas abaixo!

1. Qual comando usamos para exibir algo na tela em Python? print
Correto!

2. Como chamamos uma variável que guarda Verdadeiro ou Falso? int
Errado! A resposta era: booleano (bool)

...

=== RESULTADO FINAL ===
Você acertou 4 de 5 perguntas!
Muito bem! Continue praticando!

Jogar novamente? (s/n): n

Até logo!
```

---

## Explicação do código

### 1. Banco de perguntas com lista de dicionários
```python
perguntas = [
    {"pergunta": "1. Qual comando usamos para exibir algo na tela em Python? ",
     "respostas": ["print"], "gabarito": "print"},
    ...
]
```
Cada pergunta é um dicionário com: o texto, as respostas aceitas (lista) e o gabarito para exibir ao errar.

---

### 2. Loop automático para jogar novamente
```python
while True:
    acertos = 0
    for q in perguntas:
        ...
    continuar = input("Jogar novamente? (s/n): ").strip().lower()
    if continuar != "s":
        break
```
O `acertos` é zerado a cada rodada. O `for` percorre todas as perguntas automaticamente.

---

### 3. Verificação com lista de respostas aceitas
```python
if resposta in q["respostas"]:
    print("Correto!\n")
    acertos += 1
else:
    print(f"Errado! A resposta era: {q['gabarito']}\n")
```
`resposta in q["respostas"]` permite aceitar múltiplas respostas corretas (ex: `"bool"` e `"booleano"`).

---

## Conceitos Python utilizados

| Conceito | Uso |
|---|---|
| `list` de `dict` | Armazena as perguntas e respostas |
| `for` | Percorre todas as perguntas automaticamente |
| `in` | Verifica se a resposta está na lista de aceitas |
| `while True` + `break` | Loop para jogar novamente |
| `.strip().lower()` | Normaliza a resposta do usuário |
| f-string | Exibe resultado e gabarito formatados |

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
