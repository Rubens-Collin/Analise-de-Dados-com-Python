#Todo: Verificando os campos nulo da Base e retirando eles
#Libs para Modelagem e Matrizes
import numpy as np
import pandas as pd

#Libs para análises gráficas
import matplotlib.pyplot as plt
import seaborn as sns

#Lib para ignorar avisos
import warnings
#Desabilitando avisos
warnings.filterwarnings('ignore')


Base_Dados = pd.read_csv('PS4_GamesSales.csv', encoding='latin-1')#É necessario esse encoding para ler a base de dados

#Verificando
print(Base_Dados.head())
#Dimensão
print(Base_Dados.shape)

#Campos nulos
print('\nCampos nulos:\n',Base_Dados.isnull().sum(),'\n\n')

#Gráfico de calor com os campos nulos
plt.figure(figsize=(14,5))
plt.title('Verificando campos nulos')
sns.heatmap(Base_Dados.isnull(), cbar=False)
plt.show()
#Podemos ver que os valores que estão nulo na coluna 'Year' também estão na coluna 'Publisher'

#Retirando os campos nulos da Base #Com a função dropna eu removo os campos nulos da minha Base de Dados
Base_Dados.dropna(inplace=True)# Com o 'inplace=True' eu não preciso criar outra váriavel pra receber a Base de dados atualizada, ele já aplica diretamente na fonte dos dados
#Exemplo sem o 'inplace=True':  Base_Dados = Base_Dados.dropna()
print(Base_Dados)


#Estatiscas
print(Base_Dados.describe())

