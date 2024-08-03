!pip install pillow # Instala Pillow (caso ainda não esteja instalada)

import cv2
from google.colab.patches import cv2_imshow
from PIL import Image 
import numpy as np

# Lista de nomes das imagens
imagens = ['baleia.jpg', 'raposa.jpg', 'avengers.jpg']

# Processa cada imagem
for nome_imagem in imagens:
  try:
    # Carrega a imagem
    image_pil = Image.open('input/' + nome_imagem)
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    print(f"Imagem {nome_imagem} carregada com sucesso!")

    # Mostra a imagem original
    cv2_imshow(image)

    # Converte para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detecção de bordas
    edges = cv2.Canny(gray, 50, 150)

    # Mostra as bordas
    cv2_imshow(edges)

    # Salva a imagem de saída
    nome_saida = nome_imagem.replace('.jpg', '_visao_computacional.jpg')
    cv2.imwrite('output/' + nome_saida, edges)

  except FileNotFoundError:
    print(f"Erro: Arquivo de imagem {nome_imagem} não encontrado.")
  except Exception as e:
    print(f"Erro ao carregar a imagem {nome_imagem}: {e}")