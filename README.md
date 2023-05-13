food-image
==========

Imagens tiradas ao longo dos meses para treinamento e testes no algoritmo darknet.

# Processo de desenvolvimento #
##Pré-processamento para conversão da resolução das imagens para o formato Yolo no tamanho de 608x608. 
  Foi criado um arquivo chamado convert_image.py que lista todos os arquivos do diretório "raw" em ordem alfabética, 
converte a imagem para 608x608 e grava no diretório converted com número+jpeg, normalizando os arquivos.
##Anotando as imagens
  Utilizando o container do software label-studio.
Exemplo de uso:
Arquivo: /home/andre/label-studio.sh
!/bin/bash
sudo docker run -it -p 8080:8080 -v `pwd`/Download/PUC/:/label-studio/data heartexlabs/label-studio:latest

Autor
- __[André Eppinghaus](https://github.com/andreeppinghaus)__ 
