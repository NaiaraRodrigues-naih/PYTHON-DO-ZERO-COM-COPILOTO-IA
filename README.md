# 🐍 Python do Zero com Copiloto IA

## Semana 2 — Listas e Dicionários: Organizando Dados!

---

## O que foi feito?

Nesta semana, avançamos no aprendizado de Python! Exploramos **listas** e **dicionários**, que são maneiras poderosas de armazenar e organizar dados. Aprendemos a criar listas de itens, adicionar elementos a elas e acessar informações em dicionários usando chaves. Tudo isso de forma prática e simples para iniciantes!

---

## Conceitos Aprendidos

### O que são Listas?

Uma **lista** é como uma caixa que pode guardar vários itens em ordem. É como uma lista de compras ou uma fila de pessoas. Em Python, listas são criadas com colchetes `[]` e os itens são separados por vírgulas.

**Exemplo simples:**
```python
frutas = ["maçã", "banana", "laranja"]
```

Você pode adicionar itens à lista usando `.append()` e contar quantos itens há com `len()`.

### O que são Dicionários?

Um **dicionário** é como um livro de endereços: cada informação tem um "rótulo" (chave) associado a um valor. É perfeito para armazenar dados relacionados, como nome, idade, cidade, etc. Em Python, dicionários são criados com chaves `{}` e pares chave-valor separados por dois pontos `:`.

**Exemplo simples:**
```python
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}
```

Para acessar um valor, use a chave: `pessoa["nome"]`.

---

## Arquivo Principal: `listas_dicts.py`

Este arquivo demonstra o uso de listas e dicionários com um exemplo prático: materiais escolares e informações pessoais.

```python
# Lista de materiais escolares
materiais = ["Caderno", "Lápis de cor", "Borracha", "Caneta", "Régua", 'Mochila', "Giz de cera"]
materiais.append("Tesoura")  # Adiciona "Tesoura" à lista
print(materiais)  # Exibe a lista completa

quantidade_materiais = len(materiais)  # Conta os itens
print("Quantidade de materiais escolares: 2 de cada ")

# Dicionário de informações pessoais
informacoes_pessoais = {
    "nome": "Naiara",
    "sobrenome": "Rodrigues",
    "idade": 30,
    "cidade": "Minas Gerais"
}
print(informacoes_pessoais)  # Exibe o dicionário todo

# Acessando valores específicos
print("Nome: " + informacoes_pessoais["nome"])
print("Sobrenome: " + informacoes_pessoais["sobrenome"])
print("Idade: " + str(informacoes_pessoais["idade"]))  # Converte número para string
print("Cidade: " + informacoes_pessoais["cidade"])
```

---

## Códigos Utilizados e o que Fazem

| Código | O que faz |
|--------|-----------|
| `[]` | Cria uma **lista** vazia ou com itens |
| `{}` | Cria um **dicionário** vazio ou com pares chave-valor |
| `.append(item)` | Adiciona um item ao final da lista |
| `len(lista)` | Retorna o número de itens na lista |
| `print()` | Exibe mensagens ou valores na tela |
| `"chave"` | Acessa o valor associado à chave no dicionário |
| `str(número)` | Converte um número para string (texto) |

---

## O que o Script Faz?

Quando você roda `listas_dicts.py`, o programa:

1. Cria uma lista de materiais escolares e adiciona "Tesoura" a ela.
2. Exibe a lista completa.
3. Conta e informa a quantidade de materiais (dizendo que são 2 de cada, mas na verdade conta os itens da lista).
4. Cria um dicionário com informações pessoais.
5. Exibe o dicionário inteiro.
6. Mostra cada informação separadamente, como nome, sobrenome, idade e cidade.

**Saída esperada:**
```
['Caderno', 'Lápis de cor', 'Borracha', 'Caneta', 'Régua', 'Mochila', 'Giz de cera', 'Tesoura']
Quantidade de materiais escolares: 2 de cada
{'nome': 'Naiara', 'sobrenome': 'Rodrigues', 'idade': 30, 'cidade': 'Minas Gerais'}
Nome: Naiara
Sobrenome: Rodrigues
Idade: 30
Cidade: Minas Gerais
```

---

## Outros Arquivos na Pasta

- **`ola.py`**: Seu primeiro script, com saudações e prints básicos.
- **`variaveis.py`**: Exemplos de variáveis, concatenação e tipos de dados.

Esses arquivos são de semanas anteriores, mas ajudam a ver o progresso!

---

## Dicas para Iniciantes

- **Listas** são ótimas para coleções ordenadas de itens.
- **Dicionários** são ideais para dados estruturados com rótulos.
- Sempre use `print()` para ver o que seu código está fazendo.
- Pratique adicionando mais itens às listas e chaves aos dicionários!

Continue explorando e logo você estará criando programas incríveis! 🚀

---

*Feito com ❤️ por Naiara Rodrigues, futura dev na KenseiCyberSecurity.*

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
