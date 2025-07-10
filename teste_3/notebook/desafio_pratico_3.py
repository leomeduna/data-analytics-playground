# %%
import pandas as pd

df = pd.read_excel("C:/udemy_ds_course/teste_3/data/Desafio Prático III.xlsx")
df.head()

# Perguntas: 
# 1. Calcule a média, mediana, desvio padrão populacional e coeficiente de variação da variável Preço (R$). 
#    Identifique a moda (o valor ou os valores mais frequentes, sendo amodal - sem moda, multimodal - com várias modas ou unimodal - com uma moda, caso exista).
# 2. Crie um histograma para visualizar a distribuição dos preços. 
#    Construa um boxplot e analise a presença de outliers. 
#    Faça upload dos gráficos como imagens (formatos aceitos: PNG e JPEG). 
# 3. Avalie se a categoria do produto, aparentemente, influencia a quantidade vendida, justificando sua resposta. 
#    Utilize as ferramentas adequadas para essa análise (gráficos, tabelas, etc).
# 4. Filtre os produtos com quantidade vendida acima da mediana do conjunto. 
#    Entre esses produtos, selecione os que possuem preço superior a R$ 200 e faturament
# acima de R$ 6.000. 
#    Quantos produtos atendem a esses critérios? 
#    Qual a porcentagem em relação ao total?

# %%
media = df['Preco_R$'].sum() / len(df['Preco_R$'])
mediana = df['Preco_R$'].median()
desvio_padrao = df['Preco_R$'].std()
coef_variacao = (desvio_padrao / media) * 100
moda = df['Preco_R$'].mode()

print(f'A Média do conjunto de dados é {media}')
print(f'A Mediana do conjunto de dados é {mediana}')
print(f'O Desvio Padrão do conjunto de dados é {desvio_padrao}'),
print(f'O coeficiente de variação do conjunto de dados é {coef_variacao}')
print(f'A moda de valor do conjunto de dados é {moda}')

# %%
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6),
           dpi=400)
hist = sns.histplot(
    x=df['Preco_R$'],
    color='skyblue'
    )
plt.title("Histograma - Preço")
plt.xlabel("Preço")
plt.ylabel("Contagem")
plt.show()
# %%
boxplot = sns.boxplot(
    y=df['Preco_R$'],
    color='orange'
)
plt.title("Boxplot - Preço_R$")
plt.xlabel("Preço")
plt.ylabel("Preço")
plt.show()

# %%
df['Faturamento'] = df['Preco_R$'] * df['Quantidade_Vendida']
numerical_cols = ['Preco_R$', 'Quantidade_Vendida', 'Faturamento']

categorical_products = df.groupby('Categoria')[numerical_cols].sum()
categorical_products.sort_values(ascending=False, by='Faturamento')
# %%
sns.barplot(
    categorical_products['Faturamento'].sort_values(ascending=False),
    color='green'
)
plt.title("Soma de Faturamento entre categorias")
plt.show()

sns.barplot(
    categorical_products['Quantidade_Vendida'].sort_values(ascending=False),
    color='green'
)
plt.title("Soma de Quantidade Vendida entre categorias")
plt.show()

# Pelo visto a quantidade vendida nao influência tanto em questão de faturamento bruto
# pois como podemos ver pelo gráfico a Quantidade Vendida desse produto é a menor
# e mesmo assim é o produto que gera maior faturamento (receita).
# %%
median_filtrado = df['Quantidade_Vendida'].median()
filtro = (df['Quantidade_Vendida'] > median_filtrado) & (df['Preco_R$'] > 200) & (df['Faturamento'] > 6000)

df_filtrado = df[filtro]
df_filtrado.describe()

# 3.000 produtos atendem a estes critérios

# %%
prop_criterios = (len(df_filtrado) / len(df)) * 100 
print(f'A proporção em % de clientes que atendem aos critérios são: {prop_criterios}')