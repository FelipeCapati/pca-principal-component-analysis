# PCA - Principal Component Analysis #

## I.	 INTRODUÇÃO ##
Esse projeto tem como objetivo exemplificar a aplicação do algorítimo PCA, também chamado de ACP (Análise de
Componentes Principais) utilizado para redução de dimensionalidade de uma base de dados que tem variáveis altamente
correlacionadas.

## II.	FUNDAMENTAÇÃO TEÓRICA ##

### A.	PRINCIPAL COMPONENT ANALYSIS ###
O PCA é um acrônimo do inglês Principal Componente Analysis, em português literal é Análise de Componentes Principais.<br>
A ideia central do PCA é a redução de dimensionalidade na qual tem-se diversas variáveis de entrada com alto grau de 
correlação na qual é possível reduzir o número de variáveis altamente correlacionadas perdendo o mínimo de informação 
possível.<br>
O PCA foi desenvolvido por Karl Pearson e é fortemente utilizado em modelos preditivos e análise exploratória 
de dados. Há duas abordagens possíveis para as variáveis analisadas: Fixas ou Randomicas (em inglês denominada de
random-effects PCA). A abordagem analisada nesse projeto é a Fixa [1].<br>
O modelo do PCA é dado por:

![Alt text](images/pca-eq1.png?)

Em que:

![Alt text](images/pca-eq2.png?)

É o vetor com a média de cada variável, e:

![Alt text](images/pca-eq3.png?)

É o vetor de scores fixos e <b>W</b> é uma matrix de dimensão <b>p x q</b> que representa os dados carregados.<br>
Assumindo que o erro seja Gaussiano e de Centro zero com variância homoscedástica, podemos escreve-lo na forma de:

![Alt text](images/pca-eq4.png?)

Os parâmetros do modelo proposto é um vetor, na qual:

![Alt text](images/pca-eq5.png?)

Representa todos os parâmetros relacionados ao PCA.<br>
Existe uma abordagem estatisca para o cálculo dos parâmetros utilizando Maximum Likelihood Estimator (MLE) [1] e uma
abordagem vetorial para solucionar o problema [2] na qual seu cálculo pode ser efetuado utilizando decomposição em 
autovalores de uma matriz de covariância.<br>
O projeto vigente foi desenvolvido utilizando a segunda abordagem que, segundo [2] podemos dividi-lo nas seguintes 
etapas:<br>

1. <b>Capture os dados</b>
2. <b>Subtraia pela média</b>
3. <b>Cálcule a Matriz de Covariância</b>
4. <b>Cálculo os autovalores e os autovetores da matriz de covariância</b>
5. <b>Escolha as componentes principais</b>
6. <b>Derive para um novo dataset</b>

A concepção geométrica do problema pode ser vista no seguinte gráfico:

![Alt text](images/pca-graph01.png?)

* Na qual x1 e x2 representa os dados de entrada; 
* Փ1 e Փ2 são vetores na qual o autovalor da matriz de covariância representa a dispersão daquela variável, ou seja,
seu nível de significancia. O autovetor da matriz de covariância representa o sentido pela qual aquela dispersão aponta.

## III.	METODOLOGIA ##
Para o projeto vigente foi utilizado python juntamente com o Notebook Jupyter para prototipar o modelo do
algorítimo. Parte da base do algorítimo foi desenvolvido, ou seja, a multiplicação de matrizes, cálculo de 
matriz inversa, determinante, entre outras operações base que pode ser analisada em detalhes no path
<b>"./utilities/matrix.py"</b>.<br>
Tendo como base a fundamentação teórica abordada em II, o modelo do algorítimo esta proposto em <b>"./pca.py"</b>
na qual utiliza a funções do <b>"Numpy"</b> para o cálculo da matriz de correlação e dos autovetores e autovalores.<br>
A classe desenvolvida proporciona funções, tais como:<br>
* <b>explained_variance_ratio</b>
* <b>singular_values</b>
* <b>get_covariance</b>
* <b>fit</b>
* <b>transform</b>

Para o teste e análise do algorítimo foram propostos três datasets para executar o PCA, sendo eles:
Alps Water Dataset, Books x Grades Dataset (Análise multivariada) e o US Census Dataset. Todos os dataset
foram fornecidos pelo professor Reinaldo Bianchi. As funções obtidas foram comparados com as obtidos utilizando o LMS.

## IV. RESULTADOS ##
Os detalhes das implementações dos problemas propostos na metodologia pode ser analisados em <b>"./PCA.ipynb"</b> 
ou <b>"PCA.html"</b>.<br>
Para o problema AlpsWater temos o seguinte dataset.

![Alt text](images/alpswater-dataset.png?)

Utilizando o método dos mínimos quadrados Linear e a Análise de Componentes Principais chegamos ao seguinte gráfico.

![Alt text](images/alpswater-graph-pca-and-mmq.png?)

Para o problema Books Attend Grade, temos o seguinte dataset

![Alt text](images/books-attend-grade-dataset.png?)

Analisando o dataset do problema, teremos uma regressão multivariada, na qual o gráfico scatter a seguir
ilustra a disposição de dados no espaço.

![Alt text](images/books-attend-grade-scatter-plot.png?)

Como o problema é de multivariável, foi plotado um gráfico bidimensional que ilustra a redução da dimensiolidade, dado
um dataset com 3 variáveis foi reduzido a 2. O scatter plot são dos dados de maior significancia para a base.

![Alt text](images/books-attend-grade-graph-pca.png?)

Para o problema US Census, temos o seguinte dataset:

![Alt text](images/us-census-dataset.png?)

Na qual foi plotado o gráfico a seguir que compara as funções de reta geradas utilizando o PCA e o MMQ:

![Alt text](images/us-census-graph-pca-and-mmq.png?)

## V. CONCLUSÃO ##
Dado os resultados vistos em IV podemos inferir que o Método dos Mínimos Quadrados chegou ao resultado esperado e
graficamente é possível inferir que o erro de aproximação é relativamente baixo. Porém quando analisamos a função
que descreve o PCA é visto que há uma distância significativa entre o ponto analisado e a função de reta proposta
pelo PCA. Tal variação é esperada pelos seguintes motivos:

* Pelo fato de se tratarem de técnicas diferentes com objetivos diferentes, o MMQ busca uma função que represente 
todos os pontos dentro de um espaço, por exemplo, bidimensional. Já o PCA busca uma função que "armazene" a maior 
variação dos dados.<br>
* O PCA tem perda de significancia das variáveis, não é possível fazer uma redução de dimensionalidade sem perder 
nenhuma informação, porém o PCA visa minimizar essa perda.<br>

Um dos objetivos do projeto em curso é implementar o algorítimo do PCA. Se analisarmos os dados chegamos a conclusão de 
que o algorítimo foi implementado corretamente assim como sua comparação com o MMQ.

## VI. AGRADECIMENTOS ##

Agradecimentos especiais a CAPES e ao Centro Universitário FEI por financiar o mestrado que está em curso; 
ao professor Reinaldo Bianchi por proporcionar visões sobre o mundo acadêmico e orientar trabalhos científicos 
com o objetivo de lapidar os conhecimentos abordados em sala; aos meus pais e a minha família que sempre me 
apoiaram em meio a dificuldades.

## VII. REFERÊNCIAS ##

[1]	G. R. Naik, Advances in Principal Component Analysis: Research and Development, Editora: Springer, 2017, pág 54.<br>
[2]	R. Bianchi, Tópicos Especiais em Aprendizagem, 2019, ppt slide Centro Universitário FEI.