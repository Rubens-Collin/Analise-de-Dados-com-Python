#TODO: Criando Grids e fazendo comparações com as colunas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #Com essa biblioteca e essa função tira alguns avisos.

#Lendo a Base de Dados
Base_Dados = pd.read_csv('StudentsPerformance+(1).csv')

#Criando um gráfico de Grids
#Com a função 'pairplot' eu faço um grid com vários gráficos das variáveis numéricas
print(Base_Dados['race/ethnicity'].value_counts(normalize=True) * 100,'\n\n')
sns.pairplot(Base_Dados, hue='race/ethnicity') #Com o 'hue' eu destaco a váriavel em cores
plt.show()

#Criando um boxplot para comparar a coluna 'math score' com a coluna 'race/ethnicity'
sns.boxplot(data=Base_Dados, x='math score', y='race/ethnicity',  hue='race/ethnicity')
plt.show()

#Criando um boxplot para comparar a coluna 'math score' com a coluna 'parental level of education'
plt.figure(figsize=(15, 6))
sns.boxplot(data=Base_Dados, x='math score', y='parental level of education',  hue='parental level of education')
plt.show()
#As pessoas que tem os pais com algum tipo de graduação teve uma performace melhor na prova de matemática

#Tirando a prova da comparação da linha 26
print(Base_Dados.groupby(by=['parental level of education']).describe()['math score'].reset_index())

#Criando um boxplot para comparar a coluna 'math score' com a coluna 'test preparation course'
sns.boxplot(data=Base_Dados, x='math score', y='test preparation course', hue='test preparation course')
plt.show()
#As pessoas que se preparam para a prova teve uma performace maior.

#Tirando a prova da comparação da linha 34
print(Base_Dados.groupby(by=['test preparation course']).describe()['math score'].reset_index())




