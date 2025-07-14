# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# %%
# Função para gerar dados aleatórios
def gerar_dados(num_individuos):
    # Gerar alturas entre 1.50 e 2.00 metros
    alturas = np.random.uniform(1.50, 2.00, num_individuos)
    
    # Gerar pesos entre 50 e 120 kg
    pesos = np.random.uniform(50, 120, num_individuos)
    
    # Calcular IMC
    imc = pesos / (alturas ** 2)
    
    # Definir sexo aleatoriamente
    sexos = np.random.choice(['M', 'F'], num_individuos)
    
    # Definir problemas cardíacos com base no IMC
    problemas_cardiacos = np.where(imc > 30, 'Sim', 'Não')
    
    # Criar DataFrame
    df = pd.DataFrame({
        'Altura': alturas,
        'Peso': pesos,
        'IMC': imc,
        'Sexo': sexos,
        'Problemas Cardíacos': problemas_cardiacos
    })
    
    return df

# %%
df = gerar_dados(1000)
df.describe()

# %%
# Função para plotar gráficos de distribuição
def plotar_distribuicoes(df):
    plt.figure(figsize=(15, 10))
    
    # Histograma de Altura
    plt.subplot(2, 2, 1)
    sns.histplot(df['Altura'], bins=30, kde=True)
    plt.title('Distribuição da Altura')
    
    # Histograma de Peso
    plt.subplot(2, 2, 2)
    sns.histplot(df['Peso'], bins=30, kde=True)
    plt.title('Distribuição do Peso')
    
    # Boxplot de IMC por Sexo
    plt.subplot(2, 2, 3)
    sns.boxplot(x='Sexo', y='IMC', data=df)
    plt.title('Boxplot do IMC por Sexo')
    
    # Contagem de Problemas Cardíacos
    plt.subplot(2, 2, 4)
    sns.countplot(x='Problemas Cardíacos', data=df)
    plt.title('Contagem de Problemas Cardíacos')
    
    plt.tight_layout()
    plt.show()

plotar_distribuicoes(df)

# %%
sem_problemas_cardiacos = df['Problemas Cardíacos'] == "Não"
com_problemas_cardiacos = df['Problemas Cardíacos'] == "Sim"

df_1 = df[sem_problemas_cardiacos]
df_2 = df[com_problemas_cardiacos]

print("A média, Mediana e o Desvio padrão para os indivíduos que NÃO contém problemas cardíacos:")

print(df_1['IMC'].mean())
print(df_1['IMC'].median())
print(df_1['IMC'].std())

print("A média, Mediana e o Desvio padrão para os indivíduos que contém problemas cardíacos:")

print(df_2['IMC'].mean())
print(df_2['IMC'].median())
print(df_2['IMC'].std())

# %%
#Em suma, as distribuições de altura e peso não mostram uma simetria perfeita nem concentração acentuada em faixas estreitas. 
# A altura tende a ser mais simétrica e dispersa, enquanto o peso é menos simétrico e mais espalhado, com múltiplos picos, 
# em suas respectivas faixas.

# %%
sns.histplot(
    data=df,
    x='IMC',
    color='blue'
)
plt.title("Histograma de IMC")
plt.ylabel("Frequência")
plt.grid(True)
plt.show()
# %%
sns.histplot(
    data=df_1,
    x='IMC',
    color='blue'
)
plt.title("Histograma de IMC")
plt.ylabel("Frequência")
plt.grid(True)
plt.show()

# %%

sns.histplot(
    data=df_2,
    x='IMC',
    color='blue'
)
plt.title("Histograma de IMC")
plt.ylabel("Frequência")
plt.grid(True)
plt.show()