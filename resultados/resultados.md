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