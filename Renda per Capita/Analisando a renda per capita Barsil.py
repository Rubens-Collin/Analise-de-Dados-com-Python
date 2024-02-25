#TODO: O que é Renda Per Capita?
# A renda per capita é um dos indicadores socioeconômicos que avaliam o grau de desenvolvimento econômico de um determinado lugar. A média é obtida através da divisão do Produto Nacional Bruto (PNB) pelo número total de habitantes.
# link oficial dos dados: http://www.atlasbrasil.org.br/

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Lendo a base de dados
Base_Dados = pd.read_excel('Dados_Pib.xlsx')

# Verificando
print(Base_Dados.head(),'\n')
#Verificando o menor PIB
print(Base_Dados.loc[Base_Dados['PIB per capita'].idxmin(), ['Territorialidades', 'PIB per capita', 'Ano']], '\n')
#Verificando o maior PIB
print(Base_Dados.loc[Base_Dados['PIB per capita'].idxmax(), ['Territorialidades', 'PIB per capita', 'Ano']],'\n')
#Exemplo para printar um estado por vez
print(Base_Dados[Base_Dados['Territorialidades'] == 'São Paulo'][['Territorialidades','Ano','PIB per capita']])

print(Base_Dados.groupby( by=['Territorialidades', 'Ano'] ).mean())

#Sistema de Grids

#Cor de fundo
Cor_Fundo = '#f5f5f5'

#Criar o sistema de Grids
Grid_Graficos = sns.FacetGrid( Base_Dados, col='Territorialidades', hue='Territorialidades', col_wrap=5 ) #Com o 'col_wrap' eu escolho quantas colunas irá ter meu grid
#Com a função 'FacetGrid' eu faço um grid de um jeito muito mais simples, comparado ao arquivo de relatório

#Adicionar um gráfico de linhas em cada gráfico
Grid_Graficos = Grid_Graficos.map( plt.plot, 'Ano', 'PIB per capita' ) #'map' com esse parametro eu consigo aplicar uma função expecifica(nesse caso o plot)


#Adicionando uma sombra nos gráficos + Ajuste do título
Grid_Graficos = Grid_Graficos.map( plt.fill_between, 'Ano', 'PIB per capita', alpha=0.2 ).set_titles('{col_name} Territorialidades')
#Com o parametro 'set_titles' eu consigo fazer uma alteração no título

#Filtar o título
Grid_Graficos = Grid_Graficos.set_titles('{col_name}')#Agora eu só peguei os valores da coluna Territorialidades

#Adicionando o subtítulo
Grid_Graficos = Grid_Graficos.fig.suptitle(
    'Evolução da Renda per capita por Estado \n Essse relatório foi elaborado no treinado "Python para Análise de Dados" \n Está dispónivel no canal do youtube @Data Viking',
    fontsize=18
)

# Ajustando o subtítulo
plt.subplots_adjust(top=0.86)

plt.show()

#Com esse Grid conseguimos verificar que o 'estado' com o maior PIB é Brasilia e o estado com o menor PIB é o maranhão