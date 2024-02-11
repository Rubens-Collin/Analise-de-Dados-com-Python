#Todo: Análisando os dados da quantidade de vendas dos jogos

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

#Criando um gráfico de barras para verificar a quantidade de vendas dos jogos com a coluna 'Year' e 'Global'
plt.figure(figsize=(10, 5))
plt.title('Quantidade de Vendas Globais (mi)', loc='left', fontsize=14)
sns.barplot(data= Base_Dados, x='Year', y='Global', ci=None, color='#69b3a2', estimator=sum)
#Com o comando 'ci=None' eu retiro uma pequena barra que fica dentro das barras principais
plt.ylabel('Quantidade de Vendas (mi)')
plt.show()



