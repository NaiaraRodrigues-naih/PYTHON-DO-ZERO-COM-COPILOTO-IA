# 🐍 Python do Zero com Copiloto IA

## Semana 2 — Listas e Dicionários: Organizando Dados!

---

## O que foi feito?

Neste arquivo `listas_dicts.py`, criamos um programa simples em Python que demonstra o uso prático de **listas** e **dicionários**. Especificamente:

- **Criamos uma lista** chamada `materiais` com itens escolares iniciais.
- **Adicionamos um novo item** à lista usando o método `.append()`.
- **Contamos os itens** da lista com `len()` e exibimos uma mensagem.
- **Criamos um dicionário** chamado `informacoes_pessoais` com dados pessoais (nome, sobrenome, idade, cidade).
- **Acessamos e exibimos** cada valor do dicionário individualmente, convertendo tipos quando necessário (como idade de número para texto).
- **Criamos uma segunda lista** chamada `ferramentas_cyber` com 5 ferramentas de cibersegurança.
- **Contamos e exibimos** a quantidade de ferramentas na lista.

O código é comentado e usa `print()` para mostrar os resultados na tela, permitindo que você veja como listas e dicionários funcionam na prática. Este é um exemplo didático para iniciantes aprenderem a organizar e manipular dados em Python!

### Objetivos de Aprendizado

Com este código, você aprenderá:
- Como declarar e inicializar uma **lista** com valores.
- Como usar `.append()` para adicionar itens a uma lista.
- Como usar `len()` para contar elementos em uma lista.
- Como declarar e inicializar um **dicionário** com pares chave-valor.
- Como acessar valores em um dicionário usando chaves.
- Como concatenar strings e converter tipos (ex: `str()` para números).
- A importância de comentários (`#`) para explicar o código.
- Como usar `print()` para depurar e visualizar resultados.
- Como criar múltiplas listas em um mesmo programa para organizar diferentes tipos de dados.

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

# Lista de ferramentas de cibersegurança
ferramentas_cyber = ["Nmap", "Wireshark", "Metasploit", "Burp Suite", "John the Ripper"]
print(ferramentas_cyber)
quantidade_ferramentas = len(ferramentas_cyber)
print("Quantidade de ferramentas de cyber: " + str(quantidade_ferramentas))
```

### Explicação Linha por Linha (Para Iniciantes)

Vamos explicar o código passo a passo, como se estivéssemos aprendendo juntos!

1. **Comentário Inicial:**
   ```python
   # Lista de materiais escolares
   ```
   - Isso é um **comentário**. Começa com `#` e o Python ignora. Serve para explicar o que o código faz. Aqui, indica que vamos criar uma lista de materiais escolares.

2. **Criando a Lista:**
   ```python
   materiais = ["Caderno", "Lápis de cor", "Borracha", "Caneta", "Régua", 'Mochila', "Giz de cera"]
   ```
   - Criamos uma **lista** chamada `materiais`.
   - Colocamos itens entre `[]`, separados por vírgulas.
   - Cada item é uma **string** (texto), entre aspas.
   - Agora, `materiais` guarda esses 7 itens em ordem.

3. **Adicionando um Item:**
   ```python
   materiais.append("Tesoura")
   ```
   - Usamos `.append()` para adicionar "Tesoura" no final da lista.
   - Agora a lista tem 8 itens!

4. **Exibindo a Lista:**
   ```python
   print(materiais)
   ```
   - `print()` mostra o conteúdo da lista na tela.
   - Você verá: `['Caderno', 'Lápis de cor', 'Borracha', 'Caneta', 'Régua', 'Mochila', 'Giz de cera', 'Tesoura']`

5. **Contando os Itens:**
   ```python
   quantidade_materiais = len(materiais)
   ```
   - `len()` conta quantos itens há na lista.
   - Guardamos o resultado (8) na variável `quantidade_materiais`.

6. **Mensagem sobre Quantidade:**
   ```python
   print("Quantidade de materiais escolares: 2 de cada ")
   ```
   - Exibe uma mensagem fixa. (Nota: diz "2 de cada", mas na verdade conta os itens da lista.)

7. **Comentário para Dicionário:**
   ```python
   # Dicionário de informações pessoais
   ```
   - Outro comentário, indicando que agora vamos trabalhar com dicionário.

8. **Criando o Dicionário:**
   ```python
   informacoes_pessoais = {
       "nome": "Naiara",
       "sobrenome": "Rodrigues",
       "idade": 30,
       "cidade": "Minas Gerais"
   }
   ```
   - Criamos um **dicionário** chamado `informacoes_pessoais`.
   - Entre `{}`, colocamos pares: "chave": valor.
   - Chaves são strings (como "nome"), valores podem ser strings ou números.

9. **Exibindo o Dicionário:**
   ```python
   print(informacoes_pessoais)
   ```
   - Mostra o dicionário inteiro: `{'nome': 'Naiara', 'sobrenome': 'Rodrigues', 'idade': 30, 'cidade': 'Minas Gerais'}`

10. **Acessando Valores:**
    ```python
    print("Nome: " + informacoes_pessoais["nome"])
    ```
    - Usamos a chave "nome" para pegar o valor "Naiara".
    - Concatenamos (juntamos) com "Nome: " usando `+`.

11. **Mais Acessos:**
    - Faz o mesmo para sobrenome e cidade.
    - Para idade: `str(informacoes_pessoais["idade"])` converte o número 30 para string "30", porque `+` só funciona com textos iguais.

12. **Comentário para Nova Lista:**
    ```python
    # Lista de ferramentas de cibersegurança
    ```
    - Novo comentário indicando uma segunda lista.

13. **Criando a Lista de Ferramentas:**
    ```python
    ferramentas_cyber = ["Nmap", "Wireshark", "Metasploit", "Burp Suite", "John the Ripper"]
    ```
    - Criamos outra lista com 5 ferramentas de cibersegurança.
    - Exemplos: Nmap (scanner de rede), Wireshark (analisador de pacotes), etc.

14. **Exibindo a Lista de Ferramentas:**
    ```python
    print(ferramentas_cyber)
    ```
    - Mostra a lista: `['Nmap', 'Wireshark', 'Metasploit', 'Burp Suite', 'John the Ripper']`

15. **Contando as Ferramentas:**
    ```python
    quantidade_ferramentas = len(ferramentas_cyber)
    print("Quantidade de ferramentas de cyber: " + str(quantidade_ferramentas))
    ```
    - Conta os itens (5) e exibe a mensagem, convertendo o número para string.

---

## Ferramentas de Cibersegurança Explicadas (Para Iniciantes)

No código, criamos uma lista com 5 ferramentas populares de cibersegurança. Aqui vai uma explicação simples de cada uma, como se você estivesse começando a aprender sobre segurança digital:

1. **Nmap**:
   - **O que é?** Uma ferramenta para "mapear" redes, como um explorador que descobre dispositivos conectados.
   - **Para que serve?** Verificar quais portas estão abertas em um computador ou rede, ajudando a encontrar vulnerabilidades. É como bater na porta de uma casa para ver se alguém responde.
   - **Nível iniciante:** Use para escanear sua própria rede doméstica e aprender como funciona a conectividade.

2. **Wireshark**:
   - **O que é?** Um "espião" de pacotes de dados que viajam na internet.
   - **Para que serve?** Capturar e analisar o tráfego de rede, mostrando mensagens enviadas entre dispositivos. É como ler cartas em trânsito.
   - **Nível iniciante:** Instale e veja como seus dados viajam quando você acessa um site, para entender privacidade.

3. **Metasploit**:
   - **O que é?** Uma "caixa de ferramentas" para testar segurança, como um kit de primeiros socorros para hackers éticos.
   - **Para que serve?** Simular ataques para encontrar fraquezas em sistemas, antes que hackers maliciosos façam isso.
   - **Nível iniciante:** Aprenda conceitos de exploração de vulnerabilidades em ambientes controlados (nunca em produção sem permissão).

4. **Burp Suite**:
   - **O que é?** Um "inspetor" de aplicações web, como um detetive que examina sites.
   - **Para que serve?** Testar segurança de sites e apps web, interceptando e modificando requisições HTTP.
   - **Nível iniciante:** Use a versão gratuita para analisar como sites enviam dados e identificar riscos básicos.

5. **John the Ripper**:
   - **O que é?** Um "quebrador" de senhas, como um chaveiro que tenta chaves até abrir.
   - **Para que serve?** Testar a força de senhas, tentando "quebrá-las" com métodos como força bruta ou dicionário.
   - **Nível iniciante:** Teste senhas fracas em sua própria conta para aprender a criar senhas fortes.

**Dica importante:** Essas ferramentas são poderosas e devem ser usadas apenas para aprendizado e testes éticos. Nunca use em sistemas alheios sem permissão — isso pode ser ilegal! Comece instalando versões gratuitas e experimente em máquinas virtuais.

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

1. Cria uma lista de materiais escolares e adiciona "Tesoura".
2. Exibe a lista completa.
3. Conta e informa a quantidade de materiais.
4. Cria um dicionário com informações pessoais.
5. Exibe o dicionário inteiro.
6. Mostra cada informação separadamente.
7. Cria uma lista de 5 ferramentas de cibersegurança.
8. Exibe a lista de ferramentas.
9. Conta e informa a quantidade de ferramentas.

**Saída esperada:**
```
['Caderno', 'Lápis de cor', 'Borracha', 'Caneta', 'Régua', 'Mochila', 'Giz de cera', 'Tesoura']
Quantidade de materiais escolares: 2 de cada
{'nome': 'Naiara', 'sobrenome': 'Rodrigues', 'idade': 30, 'cidade': 'Minas Gerais'}
Nome: Naiara
Sobrenome: Rodrigues
Idade: 30
Cidade: Minas Gerais
['Nmap', 'Wireshark', 'Metasploit', 'Burp Suite', 'John the Ripper']
Quantidade de ferramentas de cyber: 5
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
- Se der erro, verifique as aspas, colchetes e chaves — eles precisam estar balanceados.

Continue explorando e logo você estará criando programas incríveis! 🚀

---

*Feito com ❤️ por Naiara Rodrigues, futura dev na KenseiCyberSecurity.*

---

## Como Rodar o Script `listas_dicts.py`?

1. Tenha o **Python** instalado no seu computador (versão 3.x recomendada).
2. Abra o terminal ou prompt de comando na pasta onde está o arquivo `listas_dicts.py`.
3. Digite o comando:

```bash
python listas_dicts.py
```

4. Pressione Enter e veja a saída na tela!

Se você tiver dúvidas, pratique rodando o código e modificando os valores para entender melhor.

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
