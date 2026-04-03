# 🐍 Python do Zero com Copiloto IA

## Semana 2 — Mão na Massa: Primeiro Script!

---

## O que foi feito?

Nesta semana dei meus primeiros passos no Python!
Escrevi meu **primeiro script** do zero, aprendi a exibir mensagens na tela e a deixar comentários no código.

---

## Arquivo criado

### `ola.py`

```python
# Meu primeiro programa em Python
print ('"Olá, Naih !"')
print("Eu sou", "um futuro dev")

# Perguntando o nome do usuário
print("Qual é o seu nome? Naiara")
print("Olá, Naiara! Seja bem-vinda ao mundo da KenseiCyberSecurity!")
```

---

## Códigos utilizados e o que fazem

| Código | O que faz |
|--------|-----------|
| `#` | **Comentário** — linha ignorada pelo Python, serve para anotar o código |
| `print()` | **Exibe uma mensagem** na tela/terminal |
| `"texto"` | **String** — representa um texto entre aspas |
| `print("a", "b")` | Exibe vários textos juntos, separados por espaço automaticamente |

---

## O que o script faz?

Quando rodado, o programa exibe mensagens de boas-vindas no terminal:

```
"Olá, Naih !"
Eu sou um futuro dev
Qual é o seu nome? Naiara
Olá, Naiara! Seja bem-vinda ao mundo da KenseiCyberSecurity!
```

---

## Como rodar o script?

1. Tenha o **Python** instalado no seu computador
2. Abra o terminal na pasta do arquivo
3. Digite o comando:

```bash
python ola.py
```

---

---

## Variáveis: Caixas com Etiquetas

### `variaveis.py`

---

### O que é uma variável?

Imagine que sua memória é um **armário cheio de caixas**.
Cada caixa guarda um valor (um nome, um número, uma frase).
Cada caixa tem uma **etiqueta** — esse é o nome da variável!

```
 ___________
|           |
|  Naiara   |  <-- valor guardado dentro da caixa
|___________|
      |
    nome        <-- etiqueta (nome da variável)
```

Em Python, você cria uma variável assim:

```python
nome = "Naiara"
#  ^       ^
#  |       |
# etiqueta  valor guardado
```

---

### O que foi feito no script `variaveis.py`?

```python
# Guardando valores em variáveis
nome = "Naiara"
sobrenome = "Rodrigues"
email = "futuradev@iniciante.com"
objetivo = "Ser uma desenvolvedora de sucesso"

# Juntando textos com +
frase = "Meu nome é " + nome + " e meu objetivo é " + objetivo + "."
print(frase)

# Juntando nome e sobrenome
nome_completo = nome + " " + sobrenome
print(nome_completo)

# Variáveis com números
ano_nascimento = 1996
idade = 2026 - ano_nascimento
print(idade)

# Número com vírgula (float)
altura = 1.70

# Estado civil (texto)
estado_civil = "Casada"
print("Minha altura é " + str(altura) + " metros e meu estado civil é " + estado_civil + ".")

# Verdadeiro ou Falso (booleano)
tem_filhos = True
print("Tenho filhos? " + str(tem_filhos))

# Número inteiro
quantos_filhos = 1
print("Quantos filhos tenho? " + str(quantos_filhos))

# Mais variáveis de texto
nome_dos_filhos = "Alicia Mariah"
print("O nome dos meus filhos é " + nome_dos_filhos)

nome_do_marido = "Weverton"
print("O nome do meu marido é " + nome_do_marido)
```

---

### Tipos de variáveis usados

| Tipo | Nome técnico | Exemplo usado no script |
|------|-------------|------------------------|
| Texto | `str` (string) | `nome = "Naiara"` |
| Número inteiro | `int` | `quantos_filhos = 1` |
| Número decimal | `float` | `altura = 1.70` |
| Verdadeiro/Falso | `bool` | `tem_filhos = True` |

---

### Códigos e conceitos usados

| Código | O que faz |
|--------|-----------|
| `variavel = valor` | Cria uma variável e guarda um valor nela |
| `+` entre textos | **Concatenação** — junta dois textos em um só |
| `str()` | Transforma número em texto para poder juntar com outros textos |
| `2026 - ano_nascimento` | Faz uma **conta matemática** com variáveis |
| `True` / `False` | Valores **booleanos** — representam verdadeiro ou falso |

---

### Regras importantes para nomear variáveis

```
✅ nome_do_marido   → correto: usa underline no lugar do espaço
❌ nome do marido   → errado: espaço não é permitido

✅ altura = 1.70    → correto: aspas só em textos, números sem aspas
❌ altura = "1.70"  → errado: assim vira texto, não número

✅ "Weverton"       → correto: texto com aspas fechadas
❌ "Weverton        → errado: faltou fechar as aspas
```

---

### O que o script exibe no terminal?

```
Naiara
Rodrigues
futuradev@iniciante.com
Ser uma desenvolvedora de sucesso
Meu nome é Naiara e meu objetivo é Ser uma desenvolvedora de sucesso.
Naiara Rodrigues
Meu nome é Naiara Rodrigues e meu objetivo é Ser uma desenvolvedora de sucesso.
30
Minha altura é 1.7 metros e meu estado civil é Casada.
Tenho filhos? True
Quantos filhos tenho? 1
O nome dos meus filhos é Alicia Mariah
O nome do meu marido é Weverton
```

---

## Sobre

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** da **Kensei Cybersecurity**.

Autora: **Naiara Rodrigues** 🚀
