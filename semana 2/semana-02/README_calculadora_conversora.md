# Projeto 1: Calculadora Conversora de Temperatura

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Script Python que converte temperaturas entre **Celsius e Fahrenheit**. O usuário escolhe a direção da conversão e digita o valor — o programa exibe o resultado formatado.

---

## Como usar

1. Execute o script no terminal:
   ```bash
   python calculadora_conversora.py
   ```

2. Escolha a opção desejada:
   ```
   === CALCULADORA CONVERSORA DE TEMPERATURA ===

   1 - Celsius para Fahrenheit
   2 - Fahrenheit para Celsius

   Escolha uma opção (1 ou 2):
   ```

3. Digite o valor e veja o resultado:
   ```
   Digite a temperatura em Celsius: 100

   Resultado: 100.0°C = 212.00°F
   ```

---

## Explicação do código

### 1. Menu de opções
```python
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

opcao = input("Escolha uma opção (1 ou 2): ")
```
Exibe as opções disponíveis e captura a escolha do usuário com `input()`. O valor digitado é armazenado como texto na variável `opcao`.

---

### 2. Conversão Celsius → Fahrenheit
```python
if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Resultado: {celsius}°C = {fahrenheit:.2f}°F")
```
- `float()` converte o texto digitado em número decimal
- Fórmula: **F = (C × 9/5) + 32**
- `:.2f` formata o resultado com 2 casas decimais

---

### 3. Conversão Fahrenheit → Celsius
```python
elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Resultado: {fahrenheit}°F = {celsius:.2f}°C")
```
- Fórmula: **C = (F − 32) × 5/9**
- Mesmo padrão: `float()` para converter e `:.2f` para formatar

---

### 4. Validação de entrada
```python
else:
    print("Opção inválida. Digite 1 ou 2.")
```
Se o usuário digitar qualquer coisa diferente de `1` ou `2`, exibe uma mensagem de erro.

---

## Conceitos Python utilizados

| Conceito | Uso no projeto |
|---|---|
| `print()` | Exibir mensagens e resultados |
| `input()` | Capturar dados do usuário |
| `float()` | Converter texto em número decimal |
| `if / elif / else` | Estrutura de decisão conforme a opção |
| f-string (`f"..."`) | Formatar o texto de saída com variáveis |
| `:.2f` | Limitar o resultado a 2 casas decimais |

---

## Fórmulas utilizadas

- **Celsius → Fahrenheit:** `F = (C × 9/5) + 32`
- **Fahrenheit → Celsius:** `C = (F − 32) × 5/9`

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
