import os
from moviepy.editor import *

def converter_gif_para_mp4(diretorio_gif, diretorio_mp4):
    # Lista todos os arquivos no diretório GIF
    arquivos_gif = [f for f in os.listdir(diretorio_gif) if f.endswith('.gif')]

    # Para cada arquivo GIF, converte para MP4
    for arquivo_gif in arquivos_gif:
        gif = os.path.join(diretorio_gif, arquivo_gif)
        mp4 = os.path.join(diretorio_mp4, os.path.splitext(arquivo_gif)[0] + '.mp4')

        # Carrega o GIF usando o MoviePy
        clip = VideoFileClip(gif)

        # Escreve o arquivo MP4
        clip.write_videofile(mp4, codec='libx264')

# Uso da função
converter_gif_para_mp4(r'C:\Users\Administrator\Desktop\ConverterWEBP\gif to mp4\salvar gifs', r'C:\Users\Administrator\Desktop\ConverterWEBP\gif to mp4\salvar mp4')
