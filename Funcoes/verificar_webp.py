# verificar_webp.py

import os
import sys
import imageio

def detect_webp_type(file_path):
    try:
        reader = imageio.get_reader(file_path)
        if len(reader) > 1:
            return "video"
        else:
            return "image"
    except Exception as e:
        print(f'Erro ao detectar o tipo do arquivo WebP {file_path}: {e}')
        return "invalid"

def verificar_webp(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print(f'Nenhum arquivo encontrado na pasta: {folder_path}')
        sys.exit(1)

    results = {"image": 0, "video": 0, "invalid": 0}

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):  # Adicione esta linha
            result = detect_webp_type(file_path)
            results[result] += 1
            print(f"{file} - Tipo: {result}")

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python verificar_webp.py [caminho_da_pasta]")
        sys.exit(1)

    folder_path = sys.argv[1]
    final_results = verificar_webp(folder_path)

    print("\nResultados finais:")
    print(f"Imagens: {final_results['image']}")
    print(f"Vídeos: {final_results['video']}")
    print(f"Inválidos: {final_results['invalid']}")
