import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pasta_origem = os.path.join(BASE_DIR, "organizador")

MAPAS_EXTENSOES = {
    "txt": "txt",
    "pdf": "pdf",
    "jpg": "imagens",
    "png": "imagens",
}

def organizar_arquivos():
    if not os.path.exists(pasta_origem):
        print(f"A pasta '{pasta_origem}' não existe.")
        return
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        if not os.path.isfile(caminho_arquivo):
            continue

        extensao = os.path.splitext(arquivo)[1][1:].lower()
        if extensao in MAPAS_EXTENSOES:
            pasta_destino = os.path.join(
                pasta_origem, 
                MAPAS_EXTENSOES[extensao]
            )
        else:
            pasta_destino = os.path.join(pasta_origem, "outros")

        os.makedirs(pasta_destino, exist_ok=True)   
        shutil.move(caminho_arquivo, pasta_destino)
        print(f"Arquivo '{arquivo}' movido para '{pasta_destino}'.")
    
if __name__ == "__main__":
    organizar_arquivos()