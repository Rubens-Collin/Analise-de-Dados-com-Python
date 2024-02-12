#TODO: Transformando os valores das colunas Publisher, Genre e Game para valores numericos
# Criando as colunas Produtor, Genero e Jogo.
# E criando gráficos para análisar cada uma delas
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


Base_Dados.dropna(inplace=True)# Com o 'inplace=True' eu não preciso criar outra váriavel pra receber a Base de dados atualizada, ele já aplica diretamente na fonte dos dados


#Retirar os anos nulos
Base_Dados = Base_Dados.loc[ (Base_Dados['Year'] != 2019) & (Base_Dados['Year']!=2020) ]#Nessa linha eu estou retirando o ano de 2019 e 2020


print(Base_Dados['Publisher'].unique())

#Transformando os valores das colunas Publisher, Genre e Game para valores numericos
#E criando novas colunas
from sklearn.preprocessing import LabelEncoder

Funcao_Label = LabelEncoder()

Base_Dados['Produtor'] = Funcao_Label.fit_transform( Base_Dados['Publisher'] )
Base_Dados['Genero'] = Funcao_Label.fit_transform( Base_Dados['Genre'] )
Base_Dados['Jogo'] = Funcao_Label.fit_transform( Base_Dados['Game'] )
print(Base_Dados.head())


#Gráfico para análisar as produtoras que mais vendeu nesses anos
Paleta_Cores = sns.color_palette('husl', 8)
plt.figure(figsize=(17, 5) )
plt.title('Análise dos Produtores de Games (mi)')
sns.scatterplot(data=Base_Dados, x='Produtor', y='Global', color=Paleta_Cores[0] )
plt.show()


#Gráfico para análisar os generos mais vendidos nesses anos
Paleta_Cores = sns.color_palette('husl', 8)
plt.figure(figsize=(17, 5) )
plt.title('Análise dos Generos de Games (mi)')
sns.scatterplot(data=Base_Dados, x='Genero', y='Global', color=Paleta_Cores[0] )
plt.show()


#Gráfico para análisar os jogos mais vendidos nesses anos
Paleta_Cores = sns.color_palette('husl', 8)
plt.figure(figsize=(17, 5) )
plt.title('Análise dos Games (mi)')
sns.scatterplot(data=Base_Dados, x='Jogo', y='Global', color=Paleta_Cores[0] )
plt.show()
