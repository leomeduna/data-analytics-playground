# Desafio Prático 5: Análise do Impacto do IMC em Problemas Cardíacos e Implicações para um Sistema de Saúde

## 📝 Visão Geral

Este diretório contém a resolução do "Desafio Prático 5" da minha jornada de aprendizado em Ciência e Análise de Dados. O foco é investigar a relação entre o Índice de Massa Corporal (IMC) e a probabilidade de ocorrência de problemas cardíacos em um conjunto de dados **simulado** de indivíduos. A análise se estende a explorar a distribuição dos IMCs e a discutir implicações conceituais para o desenvolvimento de um sistema de suporte à decisão em um ambiente hospitalar.

Este projeto complementa o "Projeto Multidisciplinar 1 (Projeto Prático 1) da Aula 23", onde foram simulados pesos e alturas, calculado o IMC e categorizados indivíduos quanto à presença de problemas cardíacos. Aqui, aprofundamos a análise estatística e conceitual desses dados.

## 🎯 Objetivos da Análise

As seguintes questões foram abordadas e respondidas nesta análise:

1.  **Impacto do IMC em Problemas Cardíacos:**
    * Comparar a média, mediana e desvio padrão do IMC entre indivíduos com e sem problemas cardíacos.
    * Gerar um gráfico de boxplot para visualizar as diferenças na distribuição do IMC entre os dois grupos e analisar se há um padrão evidente.
2.  **Distribuição dos IMCs:**
    * Criar um histograma da distribuição geral dos IMCs.
    * Avaliar se a distribuição segue um formato simétrico ou apresenta maior concentração em alguma faixa.
    * Comparar a distribuição observada com as categorias de IMC da Organização Mundial da Saúde (OMS): "Abaixo do peso", "Normal", "Sobrepeso", "Obesidade".
3.  **Representação Numérica e Arredondamento de IMC:**
    * Discutir qual conjunto numérico representa um IMC não exato (ex: 24.357896).
    * Analisar se o modelo de identificação de risco em um hospital precisaria arredondar esse número e justificar a resposta.
4.  **Utilitário do Conceito de Módulo (Valor Absoluto) na Análise do IMC:**
    * Explicar como o conceito de módulo (valor absoluto) poderia ser útil na análise do IMC.

## 📊 Dados Simulados e Apresentação

O Projeto Multidisciplinar I consiste na **simulação de dados** envolvendo pesos e alturas de indivíduos, calculando o IMC (Índice de Massa Corporal) e relacionando com dados simulados sobre a existência de problemas cardíacos. A simulação conta com **dados pseudoaleatórios gerados por simulação computacional**, e há uma **correspondência modelada matematicamente por equação e coeficientes arbitrariamente definidos** entre problemas cardíacos e a medida do IMC. Essa correspondência é aplicada para cada sexo (definidos de forma aleatória).

**Detalhes da Simulação:**
* As **alturas** são simuladas via randomização (aleatoriedade) dentro de uma faixa bem definida, utilizando o pacote `numpy.random` e a função `normal` (da distribuição normal).
* Em seguida, uma equação arbitrária é aplicada para determinar, com algum grau de aleatoriedade, os **pesos** dos indivíduos, mantendo uma correspondência teórica com as alturas.
* Logo depois, o **IMC** é calculado para cada indivíduo.
* A existência de **problemas cardíacos** (sim ou não) é definida para cada indivíduo, ambos com algum grau mínimo de correspondência com o IMC.
* Os dados gerados para cada indivíduo (Altura, Peso, IMC, Sexo, Problemas Cardíacos) são reunidos em uma **tabela (DataFrame)** para facilitar a análise.

Os dados (ou o script de geração) estão localizados na pasta `data/` deste diretório. 