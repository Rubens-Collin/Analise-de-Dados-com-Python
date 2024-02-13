#TODO: Analisando salário e experiência
# Com esses gráficos podemos chegar a conclusão que a pessoa que tem mais
# expreriência também tem o salário maior


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

Base_Dados = pd.read_csv('Salary_Data.csv')


# print(Base_Dados.head())

#Renomendo as colunas
Base_Dados.rename(columns={
    'YearsExperience' : 'Xp',
    'Salary' : 'Renda'
}, inplace=True)#Com o 'inplace=True' eu altero os nomes das colunas direto na Base

#Campos nulos
print(Base_Dados.isnull().sum())

sns.heatmap(Base_Dados.isnull(), cbar=False)
plt.show()
#Com esse gráfico podemos ver que não temos campos nulos em nossa Base

print(Base_Dados.describe())

#Analisando a coluna Renda
plt.figure( figsize=(10, 6))
plt.title('Análise da Renda')
sns.kdeplot(Base_Dados['Renda'], color='#6cc04a', shade=True)

#Analisando a coluna Xp
plt.figure( figsize=(10, 6))
plt.title('Análise de XP')
sns.kdeplot(Base_Dados['Xp'], color='#993399', shade=True)
plt.show()
#Os gráficos são bem parecidos, muito provavel que temos um corelação alta entre as colunas


# Verificando outliers
plt.figure(figsize=(10,5))
sns.boxplot( x=Base_Dados['Renda'])

plt.figure(figsize=(10,5))
sns.boxplot( x=Base_Dados['Xp'])
plt.show()
#Com esses boxplots pode ver que não temos nenhum outliers

# Distribuição
plt.figure(figsize=(10,5))
sns.scatterplot(data=Base_Dados, x='Renda', y='Xp')
#Com esse gráfico podemos ver que quanto mais experiência você tem maior é o seu sálario e vice-versa
#Com esse gráfico abaixo fica mais nítido ainda essa relação
plt.figure(figsize=(10,5))
sns.regplot(data=Base_Dados, x='Renda', y='Xp')
plt.show()


# Correlação
print(Base_Dados.corr())

#Gráfico com a correlção das colunas
Correlacao = Base_Dados.corr('pearson') #Pearson: utilazado quando as variávies andam de forma linear(correlação forte)
plt.figure(figsize=(10,5))
sns.heatmap(Correlacao, annot=True, cbar=False)#'annot=True' coloca o número dentro do quadrado do meu gráfico
#'cbar=False' tira a barra lateral

Correlacao = Base_Dados.corr('spearman') #Spearman: utilizado quando as variávies andam de forma não lineares
plt.figure(figsize=(10,5))
sns.heatmap(Correlacao, annot=True )
plt.show()