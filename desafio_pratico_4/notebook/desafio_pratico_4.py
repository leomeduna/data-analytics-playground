# %%

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %%

df = pd.read_excel("C:/udemy_ds_course/desafio_pratico_4/data/Desafio Prático IV.xlsx")
df.head(5)

# %%
filtro_menor_075 = df['IDH'] < 0.75
filtro_maior_075 = df['IDH'] >= 0.75

df_menor_075 = df[filtro_menor_075]
df_maior_075 = df[filtro_maior_075]

print(df_menor_075['PIB_per_capita'].mean())
print(df_maior_075['PIB_per_capita'].mean())

# %%
variacao_desemprego = df_menor_075['TaxaDesemprego'].mean() - df_maior_075['TaxaDesemprego'].mean()
print(variacao_desemprego)

# Podemos perceber que o índice de gini que mede a distribuição equitativa de renda, analisando a desigualdade
# pode influenciar fortemente no PIB_per_capita, ou seja, para municipios com IDH menor que 0,75, o PIB per capita
# tende a ser significativamente menor por conta da desigualdade e também da TaxaDesemprego, que com certeza influenciará
# no PIB_per_capita e por sí só já explica muito a variação no PIB por filtro de IDH, onde com o filtro de IDH menor que 0.75
# temos uma taxa de desemprego 4.31 a mais entre as médias.

# %%
# Plotando a relação entre Gini e PIB_per_capita através de gráfico de dispersão.
sns.scatterplot(
    data=df,
    x=df['Gini'],
    y=df['IDH'],
    color='blue',
    markers= 'o'
)
plt.title("IDH Vs Gini")
plt.xlabel("Gini")
plt.ylabel("IDH")
plt.grid(True)  
plt.show()

# Podemos notar que temos uma relação fortemente negativa, ou seja, conforme o Gini (Desigualdade) aumenta
# menor é o nosso IDH (índice de Desenvolvimento humano). É notavelmente claro essa relação no gráfico de dispersão.
# %%

municipios_mais_desiguais = df.groupby(by=['Municipio'])["Gini"].sum().sort_values(ascending=False)
municipios_mais_desiguais.head(3) 

# output:
# 1. Maceió | 0.61
# 2. Macapá | 0.60
# 3. Manaus | 0.60

summary = df.groupby(by=['Municipio'], as_index=False).agg(
    {
    'Gini': ['sum'],
    'PIB_per_capita': ['sum'],
    'TaxaDesemprego': ['sum'],
    'IDH': ['sum']
})

summary = summary.sort_values(
    by=[('PIB_per_capita', 'sum'), ('Gini', 'sum'), ('TaxaDesemprego', 'sum'), ('IDH', 'sum')],
    ascending=[True, False, False, True]
)
summary.head(3)


# Podemos perceber que dentre os 3 municipios que tem a maior desigualdade, a taxa de desemprego consquentemente é maior
# Além disso, o IDH é menor, estando abaixo de 0.73 e o PIB_per_capita para amostras com o IDH abaixo desse corte
# consequentemente tem média de 22.777, como vimos anteriormente.

# A metodologia para chegar nessas 3 cidades, foi uma ordenação considerando uma única medida de soma que summariza
# uma lógica dos agregados economicos, fazendo um sort para determinar as cidades com os piores indicadores.

# %%

## To-do:
# Analisar os principais desafios urbanos e sociais que essas cidades podem enfrentar com base nos dados disponíveis;
# Proposta de Políticas Públicas; 
