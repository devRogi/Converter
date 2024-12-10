# webp_to_gif.py

import os
import sys
import imageio
from Configuracoes.config import pasta_saida_mp4, pasta_saida_gifs

def criar_pasta(pasta):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

def converter_mp4_para_gif(pasta_saida_mp4, pasta_saida_gifs):
    criar_pasta(pasta_saida_gifs)

    videos_mp4 = [os.path.join(pasta_saida_mp4, arquivo) for arquivo in os.listdir(pasta_saida_mp4) if arquivo.lower().endswith('.mp4')]
    
    if not videos_mp4:
        print(f'Nenhum vídeo MP4 encontrado em {pasta_saida_mp4}')
        return

    for video_mp4 in videos_mp4:
        try:
            nome_gif = os.path.splitext(os.path.basename(video_mp4))[0]
            caminho_saida = os.path.join(pasta_saida_gifs, f'{nome_gif}.gif')
            leitor = imageio.get_reader(video_mp4)

            escritor = imageio.get_writer(caminho_saida, duration=1/leitor.get_meta_data()['fps'])

            for quadro in leitor:
                escritor.append_data(quadro)

            print(f'GIF salvo em {caminho_saida}')

        except Exception as e:
            print(f'Erro durante a conversão do vídeo para GIF ({video_mp4}): {e}')

        finally:
            leitor.close()
            escritor.close()

# Exemplo (webp to img)
if __name__ == "__main__":
    # Use as configurações do arquivo Configuracoes.py
    pasta_saida_mp4 = pasta_saida_mp4
    pasta_saida_gifs = pasta_saida_gifs

    # Chama a função de conversão
    converter_mp4_para_gif(pasta_saida_mp4, pasta_saida_gifs)

