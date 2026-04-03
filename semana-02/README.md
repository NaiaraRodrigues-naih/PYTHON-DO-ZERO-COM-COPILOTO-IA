# 🐍 Python do Zero com Copiloto IA

## Semana 2 — Listas, Dicionários, Condicionais, Loops e Funções: Organizando Dados, Tomando Decisões, Repetindo Ações e Criando Blocos Reutilizáveis!

---

## O que foi feito?

Neste projeto da Semana 2, exploramos conceitos fundamentais de Python para organizar dados, tomar decisões, repetir ações e reutilizar código. Especificamente:

- **Criamos uma lista** chamada `materiais` com itens escolares iniciais e adicionamos mais com `.append()`.
- **Contamos os itens** da lista com `len()` e exibimos mensagens.
- **Criamos um dicionário** chamado `informacoes_pessoais` com dados pessoais e acessamos valores usando chaves.
- **Criamos uma segunda lista** chamada `ferramentas_cyber` com 5 ferramentas de cibersegurança e contamos os itens.
- **Usamos estruturas condicionais** (if-else-elif) para verificar condições, como idade para maioridade, notas para classificações e respostas de um questionário.
- **Definimos funções** para reutilizar blocos de código, como saudações personalizadas e cálculos de idade.
- **Implementamos loops** (`for` e `while`) para repetir ações, como iterar sobre listas, contar números e gerar tabuadas.

O código é comentado e usa `print()` para mostrar os resultados na tela, permitindo que você veja como listas, dicionários, condicionais, loops e funções funcionam na prática. Este é um exemplo didático para iniciantes aprenderem a organizar dados, fazer o código "pensar" com decisões, automatizar repetições e reutilizar blocos de código!

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
- Como usar **estruturas condicionais** (`if`, `else`, `elif`) para tomar decisões no código com base em condições.
- Como verificar igualdade (`==`) e comparações (`>=`, `<`) em condicionais.- Como usar **loops** (`for` e `while`) para repetir ações automaticamente.
- Como iterar sobre listas com `for item in lista:`.
- Como usar `while` com condições para loops controlados.
- Como definir e chamar **funções** para reutilizar código.
- Como passar **parâmetros** para funções para personalizar seu comportamento.
- Como usar `return` para devolver valores de funções.
- Como organizar código em blocos reutilizáveis para melhor manutenção.

---

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

### O que são Funções?

Uma **função** é como uma receita ou um bloco de código que você pode reutilizar sempre que precisar. Em vez de escrever o mesmo código várias vezes, você define uma função uma vez e a chama quando quiser. Funções podem receber **parâmetros** (valores de entrada) e podem **retornar** valores. Em Python, funções são definidas com `def nome():`.

**Exemplo simples:**
```python
def saudacao():
    print("Olá!")
```

Para usar a função, chame: `saudacao()`.

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

## Arquivo Secundário: `condicionais.py`

Este arquivo demonstra o uso de **estruturas condicionais** (if-else-elif) para tomar decisões no código. É como ensinar o programa a escolher caminhos diferentes com base em condições.

```python
nome_do_candidato = "Naiara"
idade = 30
if idade >= 18:
    print(nome_do_candidato + " é maior de idade.")
else:
    print(nome_do_candidato + " é menor de idade.")

nota = 97
if nota >= 90:
    print("Parabéns! Você tirou uma nota excelente.")
elif nota >= 80 and nota < 90:
    print("Você tirou uma nota muito boa.")
else:
    print("Você tirou uma nota boa.")

# Questionário
pergunta1 = "Qual é a capital do Brasil?"
resposta1 = "Brasília"
if resposta1 == "Brasília":
    print("Resposta correta!")
else:
    print("Resposta incorreta. A capital do Brasil é Brasília.")

qual_a_cor_do_ceu = "azul"
if qual_a_cor_do_ceu == "azul":
    print("Resposta correta!")
else:
    print("Resposta incorreta. A cor do céu é azul.")

quantos_dedos_tem_a_mao = 5
if quantos_dedos_tem_a_mao == 5:
    print("Resposta correta!")
else:
    print("Resposta incorreta. A mão tem 5 dedos.")

qual_a_soma_de_2_mais_2 = 4
if qual_a_soma_de_2_mais_2 == 4:
    print("Resposta correta!")
else:
    print("Resposta incorreta. A soma de 2 + 2 é 4.")
```

### Explicação Linha por Linha (Para Iniciantes)

Vamos explicar o código passo a passo, como se estivéssemos aprendendo juntos!

1. **Verificação de Idade:**
   ```python
   nome_do_candidato = "Naiara"
   idade = 30
   if idade >= 18:
       print(nome_do_candidato + " é maior de idade.")
   else:
       print(nome_do_candidato + " é menor de idade.")
   ```
   - Define nome e idade.
   - `if idade >= 18`: Se idade for 18 ou mais, imprime "maior de idade".
   - `else`: Caso contrário, "menor de idade".

2. **Classificação de Nota:**
   ```python
   nota = 97
   if nota >= 90:
       print("Parabéns! Você tirou uma nota excelente.")
   elif nota >= 80 and nota < 90:
       print("Você tirou uma nota muito boa.")
   else:
       print("Você tirou uma nota boa.")
   ```
   - `if nota >= 90`: Excelente.
   - `elif`: Senão, se entre 80 e 89, muito boa.
   - `else`: Senão, boa.

3. **Questionário - Capital:**
   ```python
   resposta1 = "Brasília"
   if resposta1 == "Brasília":
       print("Resposta correta!")
   else:
       print("Resposta incorreta. A capital do Brasil é Brasília.")
   ```
   - Verifica se resposta é "Brasília" (igualdade com `==`).
   - Se sim, correta; senão, informa a certa.

4-6. **Outras Perguntas:**
   - Mesma lógica: verifica cor do céu, dedos na mão, soma de 2+2.
   - Usa `==` para igualdade.

---

## Arquivo Terciário: `loops.py`

Este arquivo demonstra o uso de **loops** (`for` e `while`) para repetir ações automaticamente. Loops são como "robôs" que fazem tarefas repetitivas sem você precisar escrever o mesmo código várias vezes.

```python
# FOR = para cada COR DE BLUSA FAÇA O SEGUINTE
cores_de_blusa = ["vermelha", "azul", "verde", "amarela", "preta"]
for cor in cores_de_blusa:
    print("Eu tenho uma blusa " + cor + ".")

# WHILE = ENQUANTO A CONDIÇÃO FOR VERDADEIRA, FAÇA O SEGUINTE
contador = 0
while contador < 10:
    print("Contador: " + str(contador))
    contador += 1

# Exemplo de uso do while para contar de 1 a 10 e imprimir os números pares
contador = 1
while contador <= 10:
    if contador % 2 == 0:
        print("Número par: " + str(contador))
    contador += 1

# while para contar de 1 a 10 e imprimir os números ímpares
contador = 1
while contador <= 10:
    if contador % 2 != 0:
        print("Número ímpar: " + str(contador))
    contador += 1

# while para tabuada do 10
contador = 1
while contador <= 10:
    resultado = 10 * contador
    print("10 x " + str(contador) + " = " + str(resultado))
    contador += 1

# while para uma lista de nomes
nomes = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
contador = 0
while contador < len(nomes):
    print("Nome: " + nomes[contador])
    contador += 1
```

### Explicação Linha por Linha (Para Iniciantes)

Vamos explicar o código passo a passo, como se estivéssemos aprendendo juntos!

1. **Comentário e Lista:**
   ```python
   # FOR = para cada COR DE BLUSA FAÇA O SEGUINTE
   cores_de_blusa = ["vermelha", "azul", "verde", "amarela", "preta"]
   ```
   - Cria uma lista de cores.
   - Comentário explica que o `for` vai processar cada cor.

2. **Loop For:**
   ```python
   for cor in cores_de_blusa:
       print("Eu tenho uma blusa " + cor + ".")
   ```
   - `for cor in cores_de_blusa:`: Para cada item na lista, chama de "cor".
   - Imprime uma mensagem para cada cor.

3. **Comentário While:**
   ```python
   # WHILE = ENQUANTO A CONDIÇÃO FOR VERDADEIRA, FAÇA O SEGUINTE
   contador = 0
   ```
   - Inicia contador em 0.

4. **Loop While Simples:**
   ```python
   while contador < 10:
       print("Contador: " + str(contador))
       contador += 1
   ```
   - `while contador < 10:`: Enquanto contador for menor que 10, execute.
   - Imprime o contador e aumenta em 1.

5. **While com Pares:**
   ```python
   contador = 1
   while contador <= 10:
       if contador % 2 == 0:
           print("Número par: " + str(contador))
       contador += 1
   ```
   - Conta de 1 a 10.
   - `if contador % 2 == 0:`: Se resto da divisão por 2 for 0, é par.
   - Imprime apenas pares.

6. **While com Ímpares:**
   - Similar, mas `if contador % 2 != 0:` para ímpares.

7. **Tabuada:**
   ```python
   contador = 1
   while contador <= 10:
       resultado = 10 * contador
       print("10 x " + str(contador) + " = " + str(resultado))
       contador += 1
   ```
   - Calcula e imprime tabuada do 10.

8. **While com Lista:**
   ```python
   nomes = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
   contador = 0
   while contador < len(nomes):
       print("Nome: " + nomes[contador])
       contador += 1
   ```
   - Usa contador para acessar índices da lista.
   - `len(nomes)`: Tamanho da lista (5).

---

## Arquivo Quaternário: `funcoes.py`

Este arquivo demonstra o uso de **funções** para criar blocos de código reutilizáveis. Funções são como "receitas" que você pode chamar sempre que precisar executar uma tarefa específica, evitando repetir o mesmo código várias vezes.

```python
# criando uma funcão
def saudacao():
    print("Olá! Bem-vindo ao curso de Python para Iniciantes.")
# chamando a função
saudacao()
print("Função chamada com VENCEDOR!")
# função com parâmetros
def saudacao_personalizada(nome):
    print("Olá, " + nome + "! Bem-vindo ao curso de Python para Iniciantes.")
saudacao_personalizada("Naiara")
# função com múltiplos parâmetros
def saudacao_com_idade(nome, idade):
    print("Olá, " + nome + "! Você tem " + str(idade) + " anos. Bem-vindo ao curso de Python para Iniciantes.")
saudacao_com_idade("Naiara", 30)
# função com retorno
def calcular_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    return idade
idade_calculada = calcular_idade(1996)
print("A idade calculada é: " + str(idade_calculada))
```

### Explicação Linha por Linha (Para Iniciantes)

Vamos explicar o código passo a passo, como se estivéssemos aprendendo juntos!

1. **Comentário e Definição da Função:**
   ```python
   # criando uma funcão
   def saudacao():
   ```
   - `def` é a palavra-chave para definir uma função.
   - `saudacao` é o nome da função (escolha nomes descritivos!).
   - `()` indica que não recebe parâmetros por enquanto.
   - O bloco da função vem depois, indentado.

2. **Corpo da Função:**
   ```python
       print("Olá! Bem-vindo ao curso de Python para Iniciantes.")
   ```
   - Este é o código que a função executa quando chamada.
   - Indentado com 4 espaços (padrão em Python).

3. **Chamando a Função:**
   ```python
   saudacao()
   ```
   - Para usar a função, escreva seu nome seguido de `()`.
   - Isso executa o código dentro da função.

4. **Mensagem Após Chamada:**
   ```python
   print("Função chamada com VENCEDOR!")
   ```
   - Uma mensagem normal fora da função.

5. **Função com Parâmetro:**
   ```python
   def saudacao_personalizada(nome):
   ```
   - Agora a função recebe um `parâmetro` chamado `nome`.
   - Parâmetros são valores que você passa para a função usar.

6. **Corpo com Parâmetro:**
   ```python
       print("Olá, " + nome + "! Bem-vindo ao curso de Python para Iniciantes.")
   ```
   - Usa o parâmetro `nome` na mensagem.

7. **Chamando com Argumento:**
   ```python
   saudacao_personalizada("Naiara")
   ```
   - Passa "Naiara" como argumento para o parâmetro `nome`.

8. **Função com Múltiplos Parâmetros:**
   ```python
   def saudacao_com_idade(nome, idade):
   ```
   - Recebe dois parâmetros: `nome` e `idade`.

9. **Corpo com Conversão:**
   ```python
       print("Olá, " + nome + "! Você tem " + str(idade) + " anos. Bem-vindo ao curso de Python para Iniciantes.")
   ```
   - Converte `idade` (número) para string com `str()` para concatenar.

10. **Chamando com Dois Argumentos:**
    ```python
    saudacao_com_idade("Naiara", 30)
    ```
    - Passa dois valores: "Naiara" e 30.

11. **Função com Retorno:**
    ```python
    def calcular_idade(ano_nascimento):
        idade = 2026 - ano_nascimento
        return idade
    ```
    - Calcula a idade baseada no ano de nascimento.
    - `return` devolve o valor calculado para quem chamou a função.

12. **Usando o Retorno:**
    ```python
    idade_calculada = calcular_idade(1996)
    print("A idade calculada é: " + str(idade_calculada))
    ```
    - Chama a função e guarda o resultado em `idade_calculada`.
    - Exibe o resultado.

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
| `if condição:` | Executa o bloco se a condição for verdadeira |
| `else:` | Executa o bloco se nenhuma condição anterior for verdadeira |
| `elif condição:` | Verifica outra condição se a anterior falhou |
| `==` | Verifica se dois valores são iguais |
| `>=`, `<=`, `>`, `<` | Operadores de comparação (maior ou igual, etc.) |
| `for item in lista:` | Loop que repete para cada item na lista |
| `while condição:` | Loop que repete enquanto a condição for verdadeira |
| `contador += 1` | Incrementa o contador em 1 (equivalente a `contador = contador + 1`) |
| `%` | Operador de módulo (resto da divisão, ex: `5 % 2 == 1`) |
| `def nome():` | Define uma nova função com o nome especificado |
| `return valor` | Devolve um valor da função para quem a chamou |
| `nome_funcao()` | Chama/executa a função com o nome especificado |
| `def nome(parametro):` | Define uma função que recebe um parâmetro |

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

Quando você roda `condicionais.py`, o programa:

1. Verifica se a pessoa é maior ou menor de idade com base na idade.
2. Classifica uma nota em excelente, muito boa ou boa.
3. Faz um questionário com 4 perguntas, verificando respostas e dando feedback.

Quando você roda `loops.py`, o programa:

1. Usa `for` para imprimir mensagens sobre cores de blusas.
2. Usa `while` para contar de 0 a 9.
3. Conta de 1 a 10 e imprime números pares.
4. Conta de 1 a 10 e imprime números ímpares.
5. Gera a tabuada do 10.
6. Itera sobre uma lista de nomes usando `while` e índices.

Quando você roda `funcoes.py`, o programa:

1. Define e chama uma função simples de saudação.
2. Exibe uma mensagem após chamar a função.
3. Define e chama uma função com parâmetro para saudação personalizada.
4. Define e chama uma função com múltiplos parâmetros (nome e idade).
5. Define e chama uma função que calcula idade baseada no ano de nascimento e retorna o valor.
6. Exibe o resultado do cálculo de idade.

**Saída esperada para `listas_dicts.py`:**
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

**Saída esperada para `condicionais.py`:**
```
Naiara é maior de idade.
Parabéns! Você tirou uma nota excelente.
Resposta correta!
Resposta correta!
Resposta correta!
Resposta correta!
```

**Saída esperada para `loops.py` (resumida):**
```
Eu tenho uma blusa vermelha.
Eu tenho uma blusa azul.
Eu tenho uma blusa verde.
Eu tenho uma blusa amarela.
Eu tenho uma blusa preta.
Contador: 0
Contador: 1
Contador: 2
Contador: 3
Contador: 4
Contador: 5
Contador: 6
Contador: 7
Contador: 8
Contador: 9
Número par: 2
Número par: 4
Número par: 6
Número par: 8
Número par: 10
Número ímpar: 1
Número ímpar: 3
Número ímpar: 5
Número ímpar: 7
Número ímpar: 9
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100
Nome: Alice
Nome: Bob
Nome: Charlie
Nome: Diana
Nome: Eve
```

**Saída esperada para `funcoes.py`:**
```
Olá! Bem-vindo ao curso de Python para Iniciantes.
Função chamada com VENCEDOR!
Olá, Naiara! Bem-vindo ao curso de Python para Iniciantes.
Olá, Naiara! Você tem 30 anos. Bem-vindo ao curso de Python para Iniciantes.
A idade calculada é: 30
```

---

## Arquivos na Pasta (Em Ordem de Aprendizado)

Aqui estão todos os arquivos na pasta "semana 2", organizados do inicial ao último, mostrando o progresso no aprendizado de Python:

- **`ola.py`**: O primeiro script criado, com saudações básicas e uso de `print()`.
- **`variaveis.py`**: Exemplos de variáveis, tipos de dados, concatenação e operações simples.
- **`listas_dicts.py`**: O arquivo principal desta semana, demonstrando listas e dicionários com exemplos práticos.
- **`condicionais.py`**: Exemplos de estruturas condicionais (if-else) para tomada de decisões no código.
- **`loops.py`**: Exemplos de loops (for e while) para repetir ações automaticamente.
- **`funcoes.py`**: Exemplos de funções para criar blocos de código reutilizáveis.
- **`README.md`**: Este arquivo de documentação, explicando tudo de forma didática.

Esses arquivos mostram a evolução do aprendizado, começando com conceitos básicos e avançando para estruturas de dados!

### Ordem Recomendada para Executar os Arquivos

Para acompanhar o aprendizado passo a passo, execute os arquivos nesta ordem:

1. **`ola.py`** - Primeiro script, para ver saudações básicas.
2. **`variaveis.py`** - Exemplos de variáveis e tipos de dados.
3. **`listas_dicts.py`** - Demonstração de listas e dicionários.
4. **`condicionais.py`** - Exemplos de condicionais para decisões.
5. **`loops.py`** - Exemplos de loops para repetições.

O `README.md` é para leitura e não precisa ser executado!

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
