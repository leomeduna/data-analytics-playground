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

## Resultados:
# Analisar os principais desafios urbanos e sociais que essas cidades podem enfrentar com base nos dados disponíveis;
# aumento da pobreza, exclusão social, violência, precariedade da infraestrutura e dificuldade de acesso a serviços básicos;

# Desafios Urbanos:

    #Desigualdade Espacial: A concentração de renda e oportunidades em certas áreas resulta em segregação urbana, com acesso desigual a serviços e infraestrutura.
    #Precariedade da Habitação: A falta de moradias adequadas e a ocupação de áreas de risco aumentam a vulnerabilidade a desastres naturais e criam condições insalubres.
    #Transporte Público Ineficiente: A falta de investimento no transporte público dificulta a mobilidade, especialmente para a população de baixa renda.
    #Infraestrutura Insuficiente: A escassez de saneamento básico, água potável e energia elétrica impacta a qualidade de vida, a saúde e o desenvolvimento econômico.
    #Violência Urbana: A desigualdade social e a falta de oportunidades contribuem para altas taxas de criminalidade e violência, afetando a segurança e o bem-estar.

#Desafios Sociais:

    #Pobreza e Exclusão Social: O desemprego e o baixo PIB per capita levam à pobreza e exclusão, dificultando o acesso a serviços essenciais como educação, saúde e alimentação.
    #Desigualdade de Oportunidades: A falta de acesso à educação de qualidade e a dificuldade de conseguir emprego perpetuam um ciclo de pobreza intergeracional.
    #Precarização do Trabalho: A escassez de oportunidades resulta em empregos informais e salários baixos, que não garantem uma vida digna.
    #Problemas de Saúde: A falta de acesso a serviços de saúde, saneamento e alimentação adequada contribui para o aumento de doenças e problemas de saúde pública.
    #Desigualdade de Gênero e Raça: Mulheres, negros e outras minorias enfrentam discriminação intensificada no mercado de trabalho e na sociedade.
    #Desmotivação e Desinteresse: A falta de oportunidades e a desigualdade podem gerar apatia e desinteresse na participação cívica, dificultando a busca por soluções.   

# Proposta de Políticas Públicas -

# Para combater os desafios urbanos e sociais de um município com alta desigualdade, proponho três pilares de políticas públicas:

#1. Investimento Social e Produtivo
        #Foco em reduzir a pobreza e a exclusão através de programas de transferência de renda, capacitação profissional e fomento ao empreendedorismo, gerando autonomia e novas oportunidades.

#2. Urbanização Integrada e Infraestrutura
        #Visa reduzir a desigualdade espacial por meio da regularização fundiária, investimentos em saneamento, água, energia e aprimoramento do transporte público, melhorando as condições de vida e o acesso a serviços.

#3. Fortalecimento da Educação e Saúde Pública
        #Busca romper o ciclo da pobreza garantindo acesso universal e de qualidade à educação — com escolas melhores e programas de reforço — e à saúde, com atenção primária expandida, prevenção de doenças e acesso facilitado a tratamentos.
 
