# Semana 02 — VIBE CODING Python com IA escrevendo pra você

Projetos desenvolvidos durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## Estrutura da pasta

```
semana-02/
├── 01_conversor.py
├── 02_lista_compras.py
├── 03_quiz_cyber.py
├── 04_gerador_senhas.py
└── 05_organizador.py
```

---

## Projetos

### Projeto 1 — Conversor de Temperatura `01_conversor.py`

Converte temperaturas entre **Celsius e Fahrenheit**. O usuário escolhe a direção da conversão e digita o valor.

**Conceitos:** `float()`, `input()`, `if/elif/else`, f-string, `while True`, `break`

```bash
python 01_conversor.py
```

---

### Projeto 2 — Lista de Compras `02_lista_compras.py`

Programa de lista de compras com menu interativo: **adicionar, ver, remover** itens. Salva a lista em `lista_compras.txt` ao sair.

**Conceitos:** `list`, `.append()`, `.pop()`, `enumerate()`, `open()`, `while True`

```bash
python 02_lista_compras.py
```

---

### Projeto 3 — Quiz de Cybersecurity `03_quiz_cyber.py`

Quiz com **5 perguntas de múltipla escolha** sobre segurança da informação. Cada pergunta tem **timer de 10 segundos**. Perguntas embaralhadas a cada rodada.

**Conceitos:** `threading`, `random.sample()`, `dict`, `for`, `while True`

```bash
python 03_quiz_cyber.py
```

---

### Projeto 4 — Gerador de Senhas `04_gerador_senhas.py`

Gera **5 senhas aleatórias** com base nas preferências do usuário (tamanho, maiúsculas, números, símbolos). Salva em `senhas.txt` com data e hora.

**Conceitos:** `random`, `string`, `datetime`, list comprehension, `open()` modo append

```bash
python 04_gerador_senhas.py
```

---

### Projeto 5 — Organizador de Arquivos `05_organizador.py`

Organiza arquivos de uma pasta por extensão em subpastas automáticas (Imagens, Documentos, Vídeos, Áudio, Código, Compactados, Outros). Gera log com total por categoria.

**Conceitos:** `os`, `shutil`, `dict`, `try/except`, `open()` modo append, `datetime`

```bash
python 05_organizador.py
```

---

## Como executar

1. Certifique-se de ter **Python 3.x** instalado
2. Abra o terminal na pasta `semana-02/`
3. Execute o projeto desejado:
   ```bash
   python 01_conversor.py
   ```

---

**Feito com ❤️ por Naiara Rodrigues**
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
