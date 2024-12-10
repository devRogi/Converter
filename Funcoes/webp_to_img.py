# webp_to_img.py

import os
import imageio.v2 as imageio
from Configuracoes.config import pasta_entrada_webp_img, pasta_saida_img
from Funcoes.verificar_webp import detect_webp_type

def converter_webp_para_img(pasta_entrada_webp_img, pasta_saida_img):
    # Verifica se a pasta de saída existe, se não, cria-a
    if not os.path.exists(pasta_saida_img):
        os.makedirs(pasta_saida_img)

    # Obtém a lista de imagens WebP na pasta de entrada
    imagens_webp = [os.path.join(pasta_entrada_webp_img, arquivo) for arquivo in os.listdir(pasta_entrada_webp_img) if arquivo.lower().endswith('.webp')]

    if not imagens_webp:
        print(f'Nenhuma imagem WebP encontrada em {pasta_entrada_webp_img}')
        return

    for imagem_webp in imagens_webp:
        try:
            # Verifica o tipo do arquivo WebP
            tipo = detect_webp_type(imagem_webp)
            
            # Se for uma imagem, continua com a conversão
            if tipo == "image":
                # Configuração do objeto ImageWriter
                nome_img = os.path.splitext(os.path.basename(imagem_webp))[0]
                arquivo_saida = os.path.join(pasta_saida_img, f'{nome_img}.png')
                
                # Carrega a imagem WebP e a salva como PNG
                imagem = imageio.imread(imagem_webp)
                imageio.imwrite(arquivo_saida, imagem)

                print(f'Imagem PNG salva em {arquivo_saida}')

        except Exception as e:
            print(f'Erro durante a leitura do arquivo WebP {imagem_webp}: {e}')

# Exemplo (webp to img)
if __name__ == "__main__":
    # Use as configurações do arquivo Configuracoes.py
    pasta_entrada_webp_img = pasta_entrada_webp_img
    pasta_saida_img = pasta_saida_img

    # Chama a função de conversão
    converter_webp_para_img(pasta_entrada_webp_img, pasta_saida_img)
