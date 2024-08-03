!pip install pillow # Instala Pillow (caso ainda não esteja instalada)

import cv2
from google.colab.patches import cv2_imshow
from PIL import Image 
import numpy as np

# Carrega a imagem da baleia
try:
  image_pil = Image.open('input/baleia.jpg')
  image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
  print("Imagem carregada com sucesso!")

  # Mostra a imagem original
  cv2_imshow(image)

  # Converte para escala de cinza
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Detecção de bordas
  edges = cv2.Canny(gray, 50, 150)

  # Mostra as bordas
  cv2_imshow(edges)

  # Salva a imagem de saída
  cv2.imwrite('output/baleia_visao_computacional.jpg', edges)

except FileNotFoundError:
  print("Erro: Arquivo de imagem não encontrado.")
except Exception as e:
  print(f"Erro ao carregar a imagem: {e}")