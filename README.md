food-image
==========

Imagens tiradas ao longo dos meses para treinamento e testes no algoritmo darknet.

# Processo de desenvolvimento #
## Diretório de trabalho ##
 - annotations-data 
    Diretório responsável por armazenar o banco de dados do software label-studio
 - raw
    Imagens originais sem tratamento
 - converted
    Imagens com tamanho alterado para o formato do yolo e nomes normalizados

## Pré-processamento para conversão da resolução das imagens para o formato Yolo no tamanho de 608x608. 
Foi criado um arquivo chamado convert_image.py que lista todos os arquivos do diretório "raw" em ordem alfabética, 
converte a imagem para 608x608 e grava no diretório converted com número+jpeg, normalizando os arquivos.

## Anotando as imagens
Utilizando o container do software label-studio.

Exemplo de uso:
Arquivo: /home/andre/label-studio.sh
!/bin/bash
sudo docker run -it -p 8080:8080 -v `pwd`/Download/PUC/food-image/annotations-data:/label-studio/data heartexlabs/label-studio:latest

Autor
- __[André Eppinghaus](https://github.com/andreeppinghaus)__ 
