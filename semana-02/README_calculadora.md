# Desafio Final - Script 1: Calculadora

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Calculadora simples que pede dois números e uma operação (`+`, `-`, `*`, `/`), calcula e exibe o resultado. Roda em loop automático até o usuário sair. Inclui proteção contra divisão por zero.

---

## Como usar

```bash
python calculadora.py
```

Exemplo de uso:
```
=== CALCULADORA PYTHON ===

Digite o primeiro número: 10
Digite o segundo número: 3
Escolha a operação (+, -, *, /): /

Resultado: 10.0 / 3.0 = 3.33

Fazer outro cálculo? (s/n): s

Digite o primeiro número: 5
Digite o segundo número: 0
Escolha a operação (+, -, *, /): /

Erro: não é possível dividir por zero!

Fazer outro cálculo? (s/n): n

Até logo!
```

---

## Explicação do código

### 1. Loop automático
```python
while True:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    ...
    continuar = input("Fazer outro cálculo? (s/n): ").strip().lower()
    if continuar != "s":
        break
```
`while True` mantém o programa rodando. `break` encerra quando o usuário digita `n`.

---

### 2. Operações com if/elif
```python
if operacao == "+":
    resultado = numero1 + numero2
    print(f"\nResultado: {numero1} + {numero2} = {resultado}")
elif operacao == "/":
    if numero2 == 0:
        print("\nErro: não é possível dividir por zero!")
    else:
        resultado = numero1 / numero2
        print(f"\nResultado: {numero1} / {numero2} = {resultado:.2f}")
```
Cada operação tem seu bloco. A divisão tem uma verificação extra para evitar erro ao dividir por zero.

---

## Conceitos Python utilizados

| Conceito | Uso |
|---|---|
| `float(input())` | Captura números decimais do usuário |
| `if / elif / else` | Seleciona a operação correta |
| `while True` + `break` | Loop automático com saída controlada |
| f-string + `:.2f` | Formata resultado com 2 casas decimais |
| `.strip().lower()` | Normaliza a resposta do usuário |

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
