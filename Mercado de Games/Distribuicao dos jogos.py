#TODO: Criando gráfico(boxplot) para análise da distribuição Global dos games

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

print(Base_Dados.groupby(by=['Year']).sum())

#Gráfico de análise da distribuição Global dos games
#Tamanho
plt.figure(figsize=(10,4))
#Titulo
plt.title('Análise da distribuição Global  (mi)')
sns.boxplot(data=Base_Dados, x='Year', y='Global')
plt.show()
#Podemos ver que tem bastante outliers. O principal outliers dessa base seria o GTA V no ano de 2014

print(Base_Dados.loc[Base_Dados['Global'] >= 10])
#Com esse print podemos ver os jogos mais vendidos da história do PS4 até 2018, sendo o GTA V o mais vendido

