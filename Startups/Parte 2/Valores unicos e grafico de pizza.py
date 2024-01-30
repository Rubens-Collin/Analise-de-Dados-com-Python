#Todo: Verificando campos únicos e valores únicos dentro da tabela.
# Criando um gráfico de barras com a coluna 'Setor'
# Analisando a coluna 'Pais' e verificando em quais Paises nascem as startups. Depois criando um gráfico de pizza

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #Com essa biblioteca e essa função tira alguns avisos.

#ler os dados
Base_Dados = pd.read_csv('../Startups in 2021 end.csv')

# Renomer colunas
Base_Dados.rename( columns={
    'Company' : 'Empresa',
    'Valuation ($B)' : 'Valor ($)',
    'Date Joined' : 'Data de Adesão',
    'Country' : 'Pais',
    'City' : 'Cidade',
    'Industry' : 'Setor',
    'Investors' : 'Investidores'
}, inplace=True) # Com esse parametro 'inplace=True' eu aplico essas mudanças na Base de dados


#Campo únicos (Campos que não se repete)
print('Valores únicos:\n',Base_Dados.nunique(),'\n\n')
#A função 'nunique' consegue ver os campos únicos dentro da base de dados

#Valores únicos
print('Setores únicos:\n',Base_Dados['Setor'].unique(),'\n\n')
#A função 'unique' consegue ver os valores únicos dentro de uma coluna

#Valores unicos - Rank
print(Base_Dados['Setor'].value_counts(),'\n\n')
#Valores unicos - Rank Percentual
print(round(Base_Dados['Setor'].value_counts(normalize=True) * 100),'\n\n') #A função round tira os números depois do ponto

# Fazendo um gráfico de barras
plt.figure(figsize=(15, 8))
plt.title('Analise dos Setores')
plt.bar(Base_Dados['Setor'].value_counts().index, Base_Dados['Setor'].value_counts())
plt.xticks(rotation=45, ha='right')#Essa função muda o angulo dos index do eixo X
plt.show()


#Analisando os Paises onde nasce as startups
Analise = round(Base_Dados['Pais'].value_counts(normalize=True) * 100)
print(Analise,'\n\n')

# Gráfico de Pizza
plt.figure(figsize=(15, 9))
plt.title('Analise dos Paises Geradoress de Unicornios')
plt.pie(
    Analise, #parametro
    labels = Analise.index, # para colocar os nomes dos paises no gráfico
    #shadow=True, # Coloca uma sombra no gráfico (não curti)
    startangle=90, # o start vai ser de 90°
    autopct='%1.1f%%' # coloca os valores dentro dos pedços de pizzas
)
plt.show()

# Gráfico de Pizza com os 10 primeiros index
plt.figure(figsize=(15, 6))
plt.title('Analise dos Paises Geradoress de Unicornios')
plt.pie(
    Analise.head(10), #parametro
    labels = Analise.index[0:10], # para colocar os nomes dos paises no gráfico
    startangle=90, # o start vai ser de 90°
    autopct='%1.1f%%' # coloca os valores dentro dos pedços de pizzas
)
plt.show()