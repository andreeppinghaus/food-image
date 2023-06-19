# Processo

Foram separadas 44 imagens de treinamento e 11 imagens para testes, o aprendizado possui 608 classes de comidas. Para a  configuração do total de épocas de aprendizagem, foi seguido o padrão recomendado pelo Yolo na versão 4, (2000 * 608 classes) chegando a um valor de 1.216.000 épocas.


O aprendizado começou no dia 19/05/2023 e durou uma média de 3 horas, após 1.200 iterações a função de perda estava apresentando 100%. No dia 21/05/2023 foi realizada uma nova bateria de aprendizado chegando a um total de 2400 iterações. O processo foi monitorado a cada uma hora e o darknet gera um sumário a cada 100 iterações, abaixo segue os dados referentes a evolução do processo.

iterações   função de perda
1500            0.7929
1600            0.8042
1800            0.7047
1900            0.6614
2000            0.6207
2200            0.5930
2400            0.6358

De acordo com a literatura para se conseguir os primeiros resultados, é necessário um mínimo de 4000 épocas e uma função de perda de no máximo 0.50.


# Resultados  


Data: 19/05/2023
média de 3 horas 
Você não tem uma assinatura. Saiba mais.
Disponíveis: 53.5 unidades de computação
Taxa de uso: aproximadamente 1.5 por hora


(next mAP calculation at 1200 iterations) 
 1128: 0.670639, 1.023025 avg loss, 0.001300 rate, 9.462936 seconds, 72192 images, 3319.367123 hours left
Loaded: 0.000062 seconds

Pelo retorno do map parece 

yolo v8
-------------

1000 iteracoes 1/4 - 5 (comecei a adicionar), t6 = t1+t5, t8=t6+t7, t9(1982)+t8

precisão,  é a medida de quando o modelo prevê um objto, ele estã correto em x% dos casos.

no treinamento 9, a previsão das classes é de 0.476 => 47% 
recall, é a medida de quando o modelo identifica corretamente um objeto, ele está correto em y% dos casos.

no treinamento 9, o recall é de 0.103 => 100%

nas iterações de 1 a 4, o metodo patience foi de 200, no treinamento 4, de 500 no 8/9 foi de 1500,  a partir do 9 vou colocar 1800

https://stackoverflow.com/questions/54977311/what-is-loss-cls-and-loss-bbox-and-why-are-they-always-zero-in-training

Ao treinar um detector multi-objeto, você geralmente tem (pelo menos) dois tipos de perdas:

iou
loss_bbox: uma perda que mede o quão "apertadas" as caixas delimitadoras previstas são para o objeto de verdade básica (geralmente uma perda de regressão, , L1etc. smoothL1).

loss_cls: uma perda que mede a exatidão da classificação de cada caixa delimitadora prevista: cada caixa pode conter uma classe de objeto ou um "background". Essa perda é geralmente chamada de perda de entropia cruzada.

Por que as perdas são sempre zero?
Ao treinar um detector, o modelo prevê algumas (~1K) caixas possíveis por imagem. A maioria deles está vazia (ou seja, pertence à classe "background"). A função de perda associa cada uma das caixas previstas com a anotação das caixas de verdade da imagem.

Se uma caixa predita tem uma sobreposição significativa com uma caixa de verdade básica, então loss_bboxe loss_clssão calculados para ver o quão bem o modelo é capaz de prever a caixa de verdade básica.

Por outro lado, se uma caixa predita não tiver sobreposição com nenhuma caixa de verdade básica, será loss_clscomputada apenas para a classe "background".
No entanto, se houver apenas uma sobreposição muito parcial com a verdade básica, a caixa prevista é "descartada" e nenhuma perda é computada. Suspeito que, por algum motivo, esse seja o caso da sua sessão de treinamento.

Sugiro que você verifique os parâmetros que determinam a associação entre as anotações preditas em caixa e as informações básicas. Além disso, observe os parâmetros de suas "âncoras": esses parâmetros determinam a escala e as proporções das caixas previstas.


MAP ou AP, métrica usada para medir a acurácia do yolo.

a função de perda está diminindo no treinamento 9.


Class                         Images  Instances  Box(P          R      mAP50     mAP50-95)
                   all         11         68      0.476      0.103      0.149     0.0544
  Alface, crespa, crua         11          9      0.167      0.333      0.239     0.0563
     Arroz, piamontese         11          1          0          0          0          0
 Arroz, tipo 1, cozido         11          6          0          0     0.0191    0.00642
Batata, inglesa, cozida         11          5      0.522        0.2      0.217      0.102
 Batata, inglesa, purê         11          1          1          0          0          0
     Beterraba, cozida         11          2          1          0          0          0
      Brócolis, cozido         11          1          0          0     0.0262    0.00524
Carne, bovina, capa de contra-filé, com gordura, grelhada         11          1      0.207      0.415      0.497      0.249
Carne, bovina, contra-filé, com gordura, grelhado         11          1          0          0      0.166     0.0889
Carne, bovina, fraldinha, com gordura, cozida         11          1          0          0          0          0
          Cebola, crua         11          2          0          0          0          0
Cebola, fritura, carne         11          1          1          0      0.497     0.0498
       Cenoura, cozida         11          7      0.109      0.429      0.219      0.117
         Cenoura, crua         11          5          0          0      0.405      0.102
        Chuchu, cozido         11          1          1          0          0          0
 Feijão, preto, cozido         11          8      0.437      0.296       0.31      0.106
Frango, peito, com pele, assado         11          3          1          0     0.0359    0.00756
        Inhame, cozido         11          4       0.48       0.25       0.26     0.0954
          Jiló, cozido         11          3      0.557      0.333      0.344      0.207
Ovo, de galinha, inteiro, cozido/10minutos         11          2          1          0          0          0
 Porco, pernil, assado         11          2          1          0          0          0
Tomate, com semente, cru         11          2          1          0     0.0417    0.00417
Speed: 1.5ms preprocess, 1069.7ms inference, 0.0ms loss, 8.6ms postprocess per image

https://www.mathworks.com/matlabcentral/fileexchange/104395-dual-focal-loss-dfl?s_tid=FX_rc2_behav
Results saved to runs/detect/val4

De um modo geral, a perda de DFL 'considera' o problema de desequilíbrio de classes durante o treinamento de uma NN. O desequilíbrio de classe ocorre quando há uma classe que ocorre com muita frequência e outra que ocorre menos. Por exemplo: Em imagens de rua, digamos 100 fotos, pode-se ter 200 carros e apenas 10 bicicletas. Um quer detectar carros e motos. Este é o caso de desequilíbrio de classe, quando você treina um NN, como há muitos carros, o NN aprenderá a localizar carros com precisão, enquanto as bicicletas são muito menos, pode não aprender a localizá-lo corretamente. Com a perda dfl, toda vez que o NN tenta classificar a bicicleta, há um aumento da perda. Então, agora o NN dá mais importância às aulas menos frequentes. Esta explicação é em um nível muito geral. Para saber mais, consulte o artigo sobre Perda focal e depois sobre DFL.


metricas: https://learnopencv.com/train-yolov8-on-custom-dataset/


Class                         Images  Instances   Box(P          R      mAP50     mAP50-95)
                   all         11         68      0.422     0.0981      0.169     0.0866
  Alface, crespa, crua         11          9      0.163      0.155     0.0872     0.0344
     Arroz, piamontese         11          1          0          0          0          0
 Arroz, tipo 1, cozido         11          6      0.322      0.167      0.181      0.135
Batata, inglesa, cozida         11          5       0.27        0.2      0.229      0.109
 Batata, inglesa, purê         11          1          1          0          0          0
     Beterraba, cozida         11          2          1          0          0          0
      Brócolis, cozido         11          1          0          0     0.0255     0.0051
Carne, bovina, capa de contra-filé, com gordura, grelhada         11          1          1          0      0.995      0.597
Carne, bovina, contra-filé, com gordura, grelhado         11          1          0          0     0.0829     0.0332
Carne, bovina, fraldinha, com gordura, cozida         11          1          0          0          0          0
          Cebola, crua         11          2          1          0          0          0
Cebola, fritura, carne         11          1          0          0      0.199     0.0199
       Cenoura, cozida         11          7      0.219      0.429      0.305      0.163
         Cenoura, crua         11          5      0.542       0.25      0.541      0.218
        Chuchu, cozido         11          1          1          0          0          0
 Feijão, preto, cozido         11          8      0.768      0.375      0.409      0.168
Frango, peito, com pele, assado         11          3          0          0     0.0416     0.0123
        Inhame, cozido         11          4      0.255       0.25      0.262      0.157
          Jiló, cozido         11          3      0.755      0.333      0.361      0.252
Ovo, de galinha, inteiro, cozido/10minutos         11          2          0          0          0          0
 Porco, pernil, assado         11          2          0          0          0          0
Tomate, com semente, cru         11          2          1          0          0          0
Speed: 3.5ms preprocess, 1495.7ms inference, 0.0ms loss, 7.7ms postprocess per image
Results saved to runs/detect/val7


image 1/7 /content/dataset/test/1.jpeg: 640x480 2 Arroz, tipo 1, cozidos, 1 Feijão, preto, cozido, 992.8ms
image 2/7 /content/dataset/test/2.jpeg: 640x480 (no detections), 1162.1ms
image 3/7 /content/dataset/test/3.jpeg: 640x480 1 Brócolis, cozido, 1 Porco, pernil, assado, 1192.0ms
image 4/7 /content/dataset/test/4.jpeg: 640x480 1 Feijão, preto, cozido, 1 Frango, coxa, sem pele, cozida, 963.6ms
image 5/7 /content/dataset/test/5.jpeg: 640x480 1 Cenoura, cozida, 929.6ms
image 6/7 /content/dataset/test/6.jpeg: 640x480 (no detections), 927.6ms
image 7/7 /content/dataset/test/7.jpeg: 640x480 1 Carne, bovina, acém, moído, cozido, 935.4ms
Speed: 2.4ms preprocess, 1014.7ms inference, 3.6ms postprocess per image at shape (1, 3, 640, 640)
Results saved to runs/detect/predict4