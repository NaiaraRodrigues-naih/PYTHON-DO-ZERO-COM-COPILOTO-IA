# Projeto 3: Quiz de Cybersecurity

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Quiz interativo com **5 perguntas de múltipla escolha** sobre segurança da informação. Cada pergunta tem um **timer de 10 segundos** — se o tempo acabar, a resposta conta como errada. Ao final, exibe o placar com feedback personalizado.

---

## Como usar

1. Execute o script no terminal:
   ```bash
   python quiz_cybersecurity.py
   ```

2. Para cada pergunta, escolha a opção (1, 2, 3 ou 4) antes do tempo acabar:
   ```
   === QUIZ DE CYBERSECURITY ===
   Total de perguntas: 5
   Tempo por pergunta: 10 segundos

   Pergunta 1: O que significa a sigla 'VPN'?
     1 - Virtual Private Network
     2 - Virus Protection Node
     3 - Virtual Public Network
     4 - Verified Private Node

   ⏱  Você tem 10 segundos!
   Sua resposta (1, 2, 3 ou 4): 1
   Correto!
   ```

3. Ao final, veja seu placar:
   ```
   =============================
   Resultado: 4 de 5 acertos
   Muito bem! Continue estudando!
   =============================
   ```

---

## Temas das perguntas

| # | Tema | Conceito testado |
|---|---|---|
| 1 | VPN | O que significa Virtual Private Network |
| 2 | Phishing | Ataque de engenharia social |
| 3 | 2FA | Autenticação de dois fatores |
| 4 | HTTPS | Protocolo de comunicação segura |
| 5 | Força Bruta | Ataque por tentativa e erro de senhas |

---

## Explicação do código

### 1. Banco de perguntas com dicionários
```python
perguntas = [
    {
        "pergunta": "O que significa a sigla 'VPN'?",
        "opcoes": ["1 - Virtual Private Network", ...],
        "resposta": "1"
    },
    ...
]
```
Cada pergunta é um **dicionário** com três chaves: o texto da pergunta, a lista de opções e a resposta correta. Todas as perguntas ficam numa **lista de dicionários**.

---

### 2. Timer de 10 segundos com threading
```python
import threading

def perguntar_com_timer(prompt, timeout=10):
    resposta = [None]

    def capturar():
        resposta[0] = input(prompt)

    thread = threading.Thread(target=capturar)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    return resposta[0]
```
- `threading` permite executar duas tarefas ao mesmo tempo
- A função `capturar()` roda em uma **thread separada** esperando o `input()`
- `thread.join(timeout)` faz o programa esperar no máximo 10 segundos
- Se o usuário não responder a tempo, `resposta[0]` continua `None`
- `thread.daemon = True` garante que a thread encerra junto com o programa

---

### 3. Loop pelas perguntas
```python
for i, q in enumerate(perguntas, start=1):
    print(f"\nPergunta {i}: {q['pergunta']}")
    for opcao in q["opcoes"]:
        print(f"  {opcao}")
```
- `enumerate()` percorre a lista retornando o número e o dicionário da pergunta
- `start=1` faz a contagem começar em 1
- O segundo `for` exibe cada opção da pergunta

---

### 4. Verificação da resposta e tempo esgotado
```python
resposta = perguntar_com_timer("Sua resposta (1, 2, 3 ou 4): ")

if resposta is None:
    print(f"Tempo esgotado! A resposta correta era: {opcao_certa}")
elif resposta.strip() == q["resposta"]:
    print("Correto!")
    pontos += 1
else:
    print(f"Errado! A resposta correta era: {opcao_certa}")
```
- `resposta is None` → tempo acabou antes do usuário responder
- `.strip()` remove espaços acidentais digitados pelo usuário
- `pontos += 1` incrementa o placar só em caso de acerto

---

### 5. Placar final com feedback
```python
if pontos == len(perguntas):
    print("Perfeito! Você é um expert em Cybersecurity!")
elif pontos >= 3:
    print("Muito bem! Continue estudando!")
else:
    print("Continue praticando! Você vai melhorar!")
```
Compara os pontos com o total de perguntas para dar um feedback personalizado.

---

## Conceitos Python utilizados

| Conceito | Uso no projeto |
|---|---|
| `list` | Armazena todas as perguntas do quiz |
| `dict` | Cada pergunta com suas opções e resposta |
| `for` + `enumerate()` | Percorre as perguntas com numeração |
| `threading` | Executa o timer e o input ao mesmo tempo |
| `thread.join(timeout)` | Limita o tempo de espera do input |
| `is None` | Detecta se o tempo esgotou |
| `.strip()` | Remove espaços da resposta do usuário |
| f-string | Formata as mensagens de saída |
| `if / elif / else` | Verifica resposta e exibe feedback |

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
