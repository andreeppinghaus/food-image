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

## Pré-processamento para conversão da resolução das imagens para o formato Yolo no tamanho de 608x608.  ##
Foi criado um arquivo chamado convert_image.py que lista todos os arquivos do diretório "raw" em ordem alfabética, 
converte a imagem para 608x608 e grava no diretório converted com número+jpeg, normalizando os arquivos.

## Anotando as imagens ##
Utilizando o container do software label-studio, aponte o diretório dos dados para annotations-data

### Exemplo de uso: ###
Arquivo: /home/andre/label-studio.sh
!/bin/bash
sudo docker run -it -p 8080:8080 -v `pwd`/Download/PUC/food-image/annotations-data:/label-studio/data heartexlabs/label-studio:latest

### Separando as imagens ###
Exportei as imagens para o formato do yolo.
Após separar as imagens entre treinamento e test, não posso mais misturá-las, nas outras camadas.

Criei as pastas train e test dentro do diretório annotation-images e deixei o arquivo de label, chamado classes.txt

### Realizar o download do projeto do daknet no colab, para pegar os arquivos de configuração:
!git clone https://github.com/AlexeyAB/darknet.git
!cd darknet
!make

### Montar do google drive e copiar

!cp /content/darknet/cfg/coco.names /content/gdrive/MyDrive/Colab\ Notebooks/Yolo/food-image-cfg/.
!cp /content/darknet/cfg/coco.data /content/gdrive/MyDrive/Colab\ Notebooks/Yolo/food-image-cfg/.

### Gerando arquivos de treinamento e teste
Para armazenar o nome dos arquivos jpeg para configurar quem será treinamento e teste em: train.txt e test.txt para o darknet.

cd food-image/annotation_images/train
ls *.jpeg > ../train.txt

cd food-image/annotation_images/test
ls *.jpeg > ../test.txt



Autor

- __[André Eppinghaus](https://github.com/andreeppinghaus)__ 

Referencias
    - https://labelstud.io/
    - https://www.nepa.unicamp.br/taco/tabela.php?ativo=tabela

