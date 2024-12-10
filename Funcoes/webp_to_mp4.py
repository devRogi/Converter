# webp_to_mp4.py

import os
import imageio
from Configuracoes.config import pasta_entrada_webp_mp4, pasta_saida_mp4
from Funcoes.verificar_webp import detect_webp_type

def converter_webp_para_mp4(pasta_entrada_webp_mp4, pasta_saida_mp4):
    # Verifica se a pasta de saída existe, se não, cria-a
    if not os.path.exists(pasta_saida_mp4):
        os.makedirs(pasta_saida_mp4)

    # Obtém a lista de imagens WebP na pasta de entrada
    imagens_webp = [os.path.join(pasta_entrada_webp_mp4, arquivo) for arquivo in os.listdir(pasta_entrada_webp_mp4) if arquivo.lower().endswith('.webp')]

    if not imagens_webp:
        print(f'Nenhuma imagem WebP encontrada em {pasta_entrada_webp_mp4}')
        return

    for imagem_webp in imagens_webp:
        try:
            # Verifica o tipo do arquivo WebP
            tipo = detect_webp_type(imagem_webp)
            
            # Se for um vídeo, continua com a conversão
            if tipo == "video":
                with imageio.get_reader(imagem_webp) as reader:
                    # Configuração do objeto VideoWriter
                    nome_video = os.path.splitext(os.path.basename(imagem_webp))[0]
                    arquivo_saida = os.path.join(pasta_saida_mp4, f'{nome_video}.mp4')
                    fps = 10  # Taxa de quadros desejada
                    writer = imageio.get_writer(arquivo_saida, fps=fps)

                    # Adiciona cada quadro ao vídeo
                    for quadro in reader:
                        writer.append_data(quadro)

                    print(f'Vídeo MP4 salvo em {arquivo_saida}')

                    # Fecha o escritor
                    writer.close()

        except Exception as e:
            print(f'Erro durante a leitura do arquivo WebP {imagem_webp}: {e}')

# Exemplo (webp to img)
if __name__ == "__main__":
    # Use as configurações do arquivo Configuracoes.py
    pasta_entrada_webp_mp4 = pasta_entrada_webp_mp4
    pasta_saida_mp4 = pasta_saida_mp4

    # Chama a função de conversão
    converter_webp_para_mp4(pasta_entrada_webp_mp4, pasta_saida_mp4)
