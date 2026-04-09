# Projeto 5: Organizador de Arquivos

Projeto desenvolvido durante o curso **Python do Zero com Copiloto IA** pela **KENSEI CYBERSECURITY ACADEMY**.

---

## O que o projeto faz

Script Python que **organiza arquivos de uma pasta por extensão**, movendo-os automaticamente para subpastas categorizadas (Imagens, Documentos, Vídeos, Áudio, Código, Compactados, Outros). Ao final, exibe e salva um **log completo** com o total de arquivos movidos por categoria. Roda em loop — o usuário pode organizar várias pastas sem reiniciar.

---

## Categorias suportadas

| Categoria | Extensões |
|---|---|
| Imagens | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` |
| Documentos | `.pdf` `.doc` `.docx` `.txt` `.xls` `.xlsx` `.ppt` `.pptx` |
| Vídeos | `.mp4` `.avi` `.mov` `.mkv` `.wmv` `.flv` |
| Áudio | `.mp3` `.wav` `.ogg` `.flac` `.aac` |
| Código | `.py` `.js` `.html` `.css` `.java` `.c` `.cpp` `.json` |
| Compactados | `.zip` `.rar` `.7z` `.tar` `.gz` |
| Outros | Qualquer extensão não listada |

---

## Como usar

```bash
python organizador_arquivos.py
```

Exemplo de uso:
```
=== ORGANIZADOR DE ARQUIVOS ===
Organiza por: Imagens, Documentos, Vídeos, Áudio, Código, Compactados, Outros

Digite o caminho da pasta a organizar (ou 'sair'): C:\Users\User\Downloads

Organizando 12 arquivo(s)...

  [Imagens]     foto1.jpg
  [Imagens]     foto2.png
  [Documentos]  relatorio.pdf
  [Documentos]  anotacoes.txt
  [Videos]      aula.mp4
  [Codigo]      script.py
  [Compactados] backup.zip
  [Outros]      arquivo.xyz

========== LOG DE ORGANIZAÇÃO ==========
Data:   08/04/2026 22:30:00
Pasta:  C:\Users\User\Downloads
----------------------------------------
  Codigo          1 arquivo(s)
  Compactados     1 arquivo(s)
  Documentos      2 arquivo(s)
  Imagens         2 arquivo(s)
  Outros          1 arquivo(s)
  Videos          1 arquivo(s)
----------------------------------------
  Total movidos:  8
=========================================

Log salvo em: C:\Users\User\Downloads\log_organizacao.txt

Organizar outra pasta? (s/n): n

Até logo!
```

O arquivo `log_organizacao.txt` é criado dentro da pasta organizada e acumula todos os registros.

---

## Estrutura criada na pasta

```
Downloads/
├── Imagens/
│   ├── foto1.jpg
│   └── foto2.png
├── Documentos/
│   ├── relatorio.pdf
│   └── anotacoes.txt
├── Videos/
│   └── aula.mp4
├── Codigo/
│   └── script.py
├── Compactados/
│   └── backup.zip
├── Outros/
│   └── arquivo.xyz
└── log_organizacao.txt
```

---

## Explicação do código

### 1. Dicionário de categorias
```python
CATEGORIAS = {
    "Imagens":    [".jpg", ".jpeg", ".png", ...],
    "Documentos": [".pdf", ".doc", ".docx", ...],
    ...
}
```
Cada chave é o nome da subpasta. O valor é a lista de extensões que pertencem a essa categoria. Facilita adicionar novas categorias no futuro.

---

### 2. Identificar categoria por extensão
```python
def identificar_categoria(extensao):
    ext = extensao.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if ext in extensoes:
            return categoria
    return "Outros"
```
Percorre o dicionário procurando a extensão. Se não encontrar, retorna `"Outros"`. `.lower()` garante que `.JPG` e `.jpg` sejam tratados igual.

---

### 3. Listar apenas arquivos (não pastas)
```python
arquivos = [f for f in os.listdir(caminho)
            if os.path.isfile(os.path.join(caminho, f))]
```
`os.listdir()` retorna tudo (arquivos e pastas). O filtro `os.path.isfile()` garante que só arquivos sejam processados.

---

### 4. Criar subpastas automaticamente
```python
pasta_destino = os.path.join(caminho, categoria)
os.makedirs(pasta_destino, exist_ok=True)
```
`os.makedirs()` cria a pasta se ela não existir. `exist_ok=True` evita erro se a pasta já existir.

---

### 5. Mover arquivos com shutil
```python
shutil.move(origem, destino)
contagem[categoria] = contagem.get(categoria, 0) + 1
```
`shutil.move()` move o arquivo para a pasta de destino. `contagem.get(categoria, 0)` retorna 0 se a categoria ainda não existe no dicionário, depois incrementa.

---

### 6. Log com data e hora
```python
from datetime import datetime

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

with open(log_path, "a", encoding="utf-8") as log:
    log.write(f"Data: {agora}\n")
    for categoria, qtd in sorted(contagem.items()):
        log.write(f"  {categoria:<15} {qtd} arquivo(s)\n")
```
- `datetime.now()` captura o momento exato
- `open()` com `"a"` acumula logs sem apagar registros anteriores
- `sorted()` exibe as categorias em ordem alfabética
- `:<15` alinha o texto em 15 caracteres para o log ficar organizado

---

### 7. Loop automático
```python
while True:
    caminho = input("Digite o caminho da pasta (ou 'sair'): ").strip().strip('"')
    if caminho.lower() == "sair":
        break
    organizar_pasta(caminho)
    continuar = input("Organizar outra pasta? (s/n): ").strip().lower()
    if continuar != "s":
        break
```
`.strip('"')` remove aspas que o Windows às vezes adiciona ao copiar caminhos de pasta.

---

## Bibliotecas utilizadas

| Biblioteca | Uso |
|---|---|
| `os` | Listar arquivos, criar pastas, montar caminhos |
| `shutil` | Mover arquivos entre pastas |
| `datetime` | Capturar data e hora para o log |

## Conceitos Python utilizados

| Conceito | Uso |
|---|---|
| `dict` | Mapeia categorias às extensões |
| `list comprehension` | Filtra apenas arquivos (não pastas) |
| `os.makedirs()` | Cria subpastas automaticamente |
| `shutil.move()` | Move arquivos para as subpastas |
| `dict.get()` | Contagem segura sem KeyError |
| `open()` com `"a"` | Log acumulativo em arquivo |
| `:.2f` / `:<15` | Alinhamento e formatação no log |
| `try / except` | Captura erros ao mover arquivos |
| `while True` + `break` | Loop automático com saída controlada |

---

**Feito com ❤️ por Naiara Rodrigues**  
*Estudante de Engenharia de Software — Projeto pela KenseiCyberSecurity*
