# Análise Exploratória de Dados de Preços e Vendas de Produtos

## 📝 Visão Geral

Este diretório contém a resolução de um desafio prático focado na análise exploratória de um conjunto de dados de produtos, com ênfase em estatística descritiva, visualização de dados e filtragem condicional. A tarefa visa aprofundar a compreensão sobre as características de distribuição dos preços, a relação entre categorias e vendas, e identificar produtos que atendem a critérios específicos de alto valor e faturamento.

## 🎯 Objetivos da Análise

As seguintes questões foram abordadas e respondidas nesta análise:

1.  **Estatísticas Descritivas da Variável "Preço (R$)":**
    * Calcular a média, mediana, desvio padrão populacional e coeficiente de variação.
    * Identificar a moda (se unimodal, multimodal ou amodal).
2.  **Visualização da Distribuição dos Preços e Outliers:**
    * Criar um histograma para visualizar a distribuição dos preços.
    * Construir um boxplot para analisar a presença de outliers.
    * Ambos os gráficos foram gerados e salvos como imagens (PNG ou JPEG).
3.  **Influência da Categoria na Quantidade Vendida:** Avaliar se a categoria do produto influencia, aparentemente, a quantidade vendida, utilizando ferramentas como gráficos e tabelas para justificar a resposta.
4.  **Filtragem Multi-Critério de Produtos:**
    * Filtrar produtos com quantidade vendida acima da mediana do conjunto.
    * Dentre esses, selecionar os que possuem preço superior a R$ 200 e faturamento acima de R$ 6.000.
    * Calcular quantos produtos atendem a esses critérios.
    * Calcular a porcentagem desses produtos em relação ao total.

## 📊 Dados

O conjunto de dados utilizado para esta análise contém informações sobre produtos, incluindo:
* `Preço (R$)`
* `Quantidade Vendida`
* `Categoria`

Os dados estão localizados na pasta `data/` deste diretório.