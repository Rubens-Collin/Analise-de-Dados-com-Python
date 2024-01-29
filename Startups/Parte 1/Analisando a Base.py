#TODO: Nessa primeira parte irei utiliazar a Base de Dados das startups para eu verificar
# Os dados, alterando os nomes das colunas, para que fique mais fácil
# a manipulação. E também fazer a verificação dos campos nulos, somando eles
# e fazendo um gráfico de calor.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #Com essa biblioteca e essa função tira alguns avisos.

#ler os dados
Base_Dados = pd.read_csv('../Startups in 2021 end.csv')

#Verificar a dimensão
print('SHAPE:',Base_Dados.shape,'\n')

#Primeiros registos
print('HEAD:\n',Base_Dados.head(),'\n')

#Colunas
print('COLUNAS:',Base_Dados.columns,'\n')

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

#Verificar o tipo da imformação
print(Base_Dados.info())

#Verificando os campos nulos e somando
print('\nNULOS:\n',Base_Dados.isnull().sum())


# Gráfico de calor exibindo os campos nulos da Base de Dados
plt.figure(figsize=(15, 6))
plt.title('Analisando Campos Nulos')
sns.heatmap(Base_Dados.isnull(), cbar=False)#Com o comando 'cbar=False' eu tiro a barrinha de escala, que fica do lado direito do gráfico.
plt.show()