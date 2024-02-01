#TODO: Nessa primeira parte vou fazer algumas analises da Base, como os
# campos nulos, os valores únicos e conhecimento das colunas.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #Com essa biblioteca e essa função tira alguns avisos.

#Lendo a Base de Dados
Base_Dados = pd.read_csv('StudentsPerformance+(1).csv')

#Dimensão
print(Base_Dados.shape)
print(Base_Dados.head())

#Campos Nulos. Criando um mapa de calor dos campos nulos
Nulos = Base_Dados.isnull()
plt.figure(figsize= (16, 5))
plt.title('Analise de campos nulos')
sns.heatmap(Nulos, cbar=False)
plt.show()
print('Soma dos campos nulos:\n',Nulos.sum(),'\n\n')

#Campos Únicos
print('Campos Únicos:\n',Base_Dados.nunique(),'\n\n')

#Dados duplicados
print('Dados Duplicados:',Base_Dados.duplicated().sum(),'\n\n')


# Estatistica
print('Levantamento das notas: \n',Base_Dados.describe(),'\n\n')

#Informações da Base
print(Base_Dados.info())

