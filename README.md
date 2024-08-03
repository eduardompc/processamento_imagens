# Visão Computacional com OpenCV

Este projeto demonstra o uso da biblioteca OpenCV para realizar processamento de imagens em Python, no ambiente Google Colab. O código aplica detecção de bordas em imagens e salva os resultados.

## Requisitos

* Python 3.x
* OpenCV
* Pillow
* NumPy

## Instalação

1. Instale as bibliotecas necessárias:
bash pip install opencv-python pillow numpy

## Uso

1. **Crie as pastas:** Certifique-se de que as pastas `input` e `output` existam no mesmo diretório do seu notebook.
2. **Coloque as imagens:** Coloque as imagens que deseja processar na pasta `input`.
3. **Execute o código:** Execute o código Python fornecido no seu ambiente Google Colab.
4. **Verifique os resultados:** As imagens processadas com detecção de bordas serão salvas na pasta `output`.

## Exemplo

O código processa três imagens: `baleia.jpg`, `raposa.jpg` e `avengers.jpg`. Para cada imagem, ele:

1. Carrega a imagem da pasta `input`.
2. Converte a imagem para escala de cinza.
3. Aplica o algoritmo Canny para detecção de bordas.
4. Mostra a imagem original e a imagem com as bordas detectadas.
5. Salva a imagem processada na pasta `output`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto é licenciado sob a licença MIT.

## Utilização fora do Google Colab

Para executar este código em outro ambiente Python, siga estes passos:

1. **Instale as bibliotecas:** Certifique-se de ter as bibliotecas OpenCV, Pillow e NumPy instaladas. Utilize o comando `pip`:
bash pip install opencv-python pillow numpy
2. **Adapte o código:** Substitua as linhas que utilizam `cv2_imshow` (específico do Google Colab) por `cv2.imshow` e as funções auxiliares do OpenCV para exibir as imagens:
python cv2.imshow('Imagem Original', image) cv2.waitKey(0) cv2.destroyAllWindows()

cv2.imshow('Bordas Detectadas', edges) cv2.waitKey(0) cv2.destroyAllWindows()
3. **Execute o código:** Salve o código em um arquivo Python (por exemplo, `processamento_imagens.py`) e execute-o no seu terminal:
bash python processamento_imagens.py
Certifique-se de que as pastas `input` e `output` estejam no mesmo diretório do arquivo Python que você executar.
