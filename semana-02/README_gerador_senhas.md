# Projeto 4: Gerador de Senhas

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Gera **5 senhas aleatórias de uma vez** com base nas preferências do usuário (tamanho, maiúsculas, números e símbolos). As senhas são exibidas no terminal e **salvas automaticamente em `senhas.txt`** com data e hora. O programa roda em loop até o usuário decidir sair.

---

## Como usar

1. Execute o script no terminal:
   ```bash
   python gerador_senhas.py
   ```

2. Responda às perguntas de configuração:
   ```
   === GERADOR DE SENHAS ===
   Gera 5 senhas por vez e salva em senhas.txt

   Tamanho da senha (mínimo 6): 12
   Incluir letras maiúsculas? (s/n): s
   Incluir números? (s/n): s
   Incluir símbolos (!@#...)? (s/n): n
   ```

3. As 5 senhas aparecem e são salvas:
   ```
   --- 5 senhas geradas ---
     1. mK3aRvqe2xLp
     2. bW7nQjz4YcRe
     3. pA2sXkm8VoLt
     4. rN5hZwc1MqBe
     5. gT9uFdx6KjWn

   Senhas salvas em 'senhas.txt' com data e hora!

   Gerar mais senhas? (s/n): n

   Até logo!
   ```

4. O arquivo `senhas.txt` acumula todas as gerações:
   ```
   ========================================
   Data: 08/04/2026 22:15:30
   Tamanho: 12 | Tipos: Maiúsculas, Números
   ========================================
   1. mK3aRvqe2xLp
   2. bW7nQjz4YcRe
   3. pA2sXkm8VoLt
   4. rN5hZwc1MqBe
   5. gT9uFdx6KjWn
   ```

---

## Explicação do código

### 1. Bibliotecas importadas
```python
import random
import string
from datetime import datetime
```
- `random` — sorteia os caracteres aleatoriamente
- `string` — fornece conjuntos prontos de letras e números (`ascii_lowercase`, `digits`, etc.)
- `datetime` — captura a data e hora atual para registrar no arquivo

---

### 2. Conjuntos de caracteres
```python
MINUSCULAS = string.ascii_lowercase   # abcdefghijklmnopqrstuvwxyz
MAIUSCULAS = string.ascii_uppercase   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
NUMEROS    = string.digits            # 0123456789
SIMBOLOS   = "!@#$%&*()_+-=[]{}?"
```
Cada conjunto é uma string de caracteres disponíveis para compor a senha.

---

### 3. Função gerar_senha()
```python
def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    caracteres = MINUSCULAS
    obrigatorios = []

    if usar_maiusculas:
        caracteres += MAIUSCULAS
        obrigatorios.append(random.choice(MAIUSCULAS))
    ...

    restante = tamanho - len(obrigatorios)
    senha = obrigatorios + [random.choice(caracteres) for _ in range(restante)]
    random.shuffle(senha)
    return "".join(senha)
```
- Monta o conjunto de caracteres com base nas escolhas do usuário
- Insere **1 caractere obrigatório** de cada tipo ativado — garante que a senha sempre tenha o tipo escolhido
- Preenche o restante com caracteres aleatórios do conjunto total
- `random.shuffle()` embaralha a lista para que os obrigatórios não fiquem sempre no início
- `"".join()` transforma a lista de caracteres numa string

---

### 4. Geração de 5 senhas de uma vez
```python
senhas = [gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
          for _ in range(QUANTIDADE)]
```
**List comprehension** — cria uma lista chamando `gerar_senha()` 5 vezes com as mesmas configurações. O `_` é usado quando a variável do loop não é necessária.

---

### 5. Função salvar_senhas() — salva em arquivo com data
```python
def salvar_senhas(senhas, tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("senhas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Data: {agora}\n")
        for i, senha in enumerate(senhas, start=1):
            arquivo.write(f"{i}. {senha}\n")
```
- `datetime.now()` captura o momento exato
- `.strftime()` formata a data como `08/04/2026 22:15:30`
- `open()` com `"a"` — modo **append**: adiciona ao arquivo sem apagar o conteúdo anterior
- `encoding="utf-8"` — suporte a acentos e caracteres especiais

---

### 6. Loop automático
```python
while True:
    ...
    continuar = input("Gerar mais senhas? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nAté logo!")
        break
```
O programa continua gerando senhas até o usuário digitar `n`. Cada rodada acumula no mesmo `senhas.txt`.

---

## Conceitos Python utilizados

| Conceito | Uso no projeto |
|---|---|
| `import string` | Conjuntos prontos de letras e números |
| `import random` | Sorteio aleatório de caracteres |
| `from datetime import datetime` | Captura data e hora atual |
| `random.choice()` | Escolhe 1 caractere aleatório |
| `random.shuffle()` | Embaralha a lista de caracteres |
| `"".join()` | Converte lista em string |
| List comprehension | Gera 5 senhas em uma linha |
| `open()` com `"a"` | Abre arquivo em modo append |
| `.strftime()` | Formata data e hora |
| `while True` + `break` | Loop automático com saída controlada |
| `enumerate()` | Numera as senhas ao exibir e salvar |

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
