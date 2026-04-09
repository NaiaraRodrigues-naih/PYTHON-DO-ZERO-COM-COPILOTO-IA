# Projeto 5: Organizador de Arquivos
# Organiza arquivos por extensão em subpastas. Gera log com total por categoria.

import os
import shutil
from datetime import datetime

CATEGORIAS = {
    "Imagens":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"],
    "Videos":     [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"],
    "Audio":      [".mp3", ".wav", ".ogg", ".flac", ".aac"],
    "Codigo":     [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".ts", ".json"],
    "Compactados":[".zip", ".rar", ".7z", ".tar", ".gz"],
    "Outros":     []
}


def identificar_categoria(extensao):
    ext = extensao.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if ext in extensoes:
            return categoria
    return "Outros"


def organizar_pasta(caminho):
    if not os.path.isdir(caminho):
        print(f"\nPasta não encontrada: {caminho}")
        return

    arquivos = [f for f in os.listdir(caminho)
                if os.path.isfile(os.path.join(caminho, f))
                and f != "log_organizacao.txt"]

    if not arquivos:
        print("\nNenhum arquivo encontrado na pasta.")
        return

    contagem = {}
    erros = 0

    print(f"\nOrganizando {len(arquivos)} arquivo(s)...\n")

    for arquivo in arquivos:
        _, extensao = os.path.splitext(arquivo)
        categoria = identificar_categoria(extensao)

        pasta_destino = os.path.join(caminho, categoria)
        os.makedirs(pasta_destino, exist_ok=True)

        origem = os.path.join(caminho, arquivo)
        destino = os.path.join(pasta_destino, arquivo)

        try:
            shutil.move(origem, destino)
            contagem[categoria] = contagem.get(categoria, 0) + 1
            print(f"  [{categoria}] {arquivo}")
        except Exception as e:
            print(f"  [ERRO] {arquivo}: {e}")
            erros += 1

    # Log
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total = sum(contagem.values())

    print("\n========== LOG DE ORGANIZAÇÃO ==========")
    print(f"Data:   {agora}")
    print(f"Pasta:  {caminho}")
    print(f"----------------------------------------")
    for categoria, qtd in sorted(contagem.items()):
        print(f"  {categoria:<15} {qtd} arquivo(s)")
    print(f"----------------------------------------")
    print(f"  Total movidos:  {total}")
    if erros:
        print(f"  Erros:          {erros}")
    print("=========================================")

    # Salva log em arquivo
    log_path = os.path.join(caminho, "log_organizacao.txt")
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"\n{'=' * 40}\n")
        log.write(f"Data: {agora}\n")
        log.write(f"Pasta: {caminho}\n")
        log.write(f"{'-' * 40}\n")
        for categoria, qtd in sorted(contagem.items()):
            log.write(f"  {categoria:<15} {qtd} arquivo(s)\n")
        log.write(f"{'-' * 40}\n")
        log.write(f"  Total: {total} arquivo(s) movidos\n")
        if erros:
            log.write(f"  Erros: {erros}\n")

    print(f"\nLog salvo em: {log_path}")


print("=== ORGANIZADOR DE ARQUIVOS ===")
print("Organiza por: Imagens, Documentos, Vídeos, Áudio, Código, Compactados, Outros")

while True:
    print()
    caminho = input("Digite o caminho da pasta a organizar (ou 'sair'): ").strip().strip('"')

    if caminho.lower() == "sair":
        print("\nAté logo!")
        break

    organizar_pasta(caminho)

    print()
    continuar = input("Organizar outra pasta? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nAté logo!")
        break
