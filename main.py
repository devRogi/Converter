# main.py

import subprocess
import os
import sys
from datetime import datetime
from Configuracoes.config import folder_path
from Funcoes import webp_to_gif, verificar_webp, webp_to_img, webp_to_mp4
from Configuracoes.config import (pasta_saida_mp4, pasta_saida_gifs, 
                                  pasta_entrada_webp_img, pasta_saida_img, 
                                  pasta_entrada_webp_mp4, file_path)

def executar_script(script, *args):
    try:
        subprocess.run(["python", script, *args])
    except Exception as e:
        print(f'Erro ao executar o script {script}: {e}')

def criar_pasta(base_path, subfolder_name):
    # Cria uma pasta baseada na data e hora atual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"{subfolder_name}_{timestamp}"
    folder_path = os.path.join(base_path, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path

def detectar_formato_pasta(folder_path):
    imagens_count = 0
    videos_count = 0

    try:
        result = subprocess.run(["python", "verificar_webp.py", folder_path], capture_output=True, text=True)
        linhas = result.stdout.splitlines()
        for linha in linhas:
            if "Tipo: image" in linha:
                imagens_count += 1
            elif "Tipo: video" in linha:
                videos_count += 1
    except Exception as e:
        print(f'Erro ao detectar o formato da pasta {folder_path}: {e}')

    return imagens_count, videos_count

def converter_arquivos(tipo):
    try:
        verificar_webp.detect_webp_type(file_path)
        if tipo in ["mp4", "todos"]:
            webp_to_mp4.converter_webp_para_mp4(pasta_entrada_webp_mp4, pasta_saida_mp4)
        if tipo in ["gif", "todos"]:
            webp_to_gif.converter_mp4_para_gif(pasta_saida_mp4, pasta_saida_gifs)
        if tipo in ["png", "todos"]:
            webp_to_img.converter_webp_para_img(pasta_entrada_webp_img, pasta_saida_img)
    except Exception as e:
        print(f'Erro ao converter arquivos: {e}')

def converter_webp(folder_path, pasta_saida):
    pasta_saida_geral = criar_pasta(pasta_saida, "output")
    result = subprocess.run(["python", "verificar_webp.py", folder_path], capture_output=True, text=True)
    linhas = result.stdout.splitlines()

    for linha in linhas:
        nome_arquivo, tipo = linha.split(" - Tipo: ")
        pasta_saida_arquivo = criar_pasta(pasta_saida_geral, nome_arquivo)

        try:
            if tipo == "image":
                executar_script("webp_to_img.py", pasta_saida_arquivo)
            elif tipo == "video":
                executar_script("webp_to_mp4.py", pasta_saida_arquivo)
                executar_script("webp_to_gif.py", pasta_saida_arquivo)
        except Exception as e:
            print(f'Erro ao converter o arquivo {nome_arquivo} para {tipo}: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py [tipo]")
        sys.exit(1)

    tipo = sys.argv[1]
    pasta_saida = criar_pasta(folder_path, "output")
    converter_arquivos(tipo)
    converter_webp(folder_path, pasta_saida)
