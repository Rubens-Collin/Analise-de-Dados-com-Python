#Todo: Juntando todos os gráficos e colocando em um subplots
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

##Todo: Verificando os campos nulo da Base e retirando eles
# print(Base_Dados.head())
# #Dimensão
# print(Base_Dados.shape)

# #Campos nulos
# print('\nCampos nulos:\n',Base_Dados.isnull().sum(),'\n\n')

#Gráfico de calor com os campos nulos
# plt.figure(figsize=(14,5))
# plt.title('Verificando campos nulos')
# sns.heatmap(Base_Dados.isnull(), cbar=False)
# plt.show()
#Podemos ver que os valores que estão nulo na coluna 'Year' também estão na coluna 'Publisher'

#Retirando os campos nulos da Base #Com a função dropna eu removo os campos nulos da minha Base de Dados
Base_Dados.dropna(inplace=True)# Com o 'inplace=True' eu não preciso criar outra váriavel pra receber a Base de dados atualizada, ele já aplica diretamente na fonte dos dados
#Exemplo sem o 'inplace=True':  Base_Dados = Base_Dados.dropna()
# print(Base_Dados)


#Estatiscas
# print(Base_Dados.describe())

#Todo: Análisando os dados da quantidade de vendas dos jogos


#Criando um gráfico de barras para verificar a quantidade de vendas dos jogos com a coluna 'Year' e 'Global'
# plt.figure(figsize=(10, 5))
# plt.title('Quantidade de Vendas Globais (mi)', loc='left', fontsize=14)
# sns.barplot(data= Base_Dados, x='Year', y='Global', ci=None, color='#69b3a2', estimator=sum)
# #Com o comando 'ci=None' eu retiro uma pequena barra que fica dentro das barras principais
# plt.ylabel('Quantidade de Vendas (mi)')
# plt.show()

#TODO: Retirando os anos nulos(2019 e 2020) da minha Base de Dados
# Criando um gráfico com a curva de distribuição do valor de vendas

#Retirar os anos nulos
Base_Dados = Base_Dados.loc[ (Base_Dados['Year'] != 2019) & (Base_Dados['Year']!=2020) ]#Nessa linha eu estou retirando o ano de 2019 e 2020
#Com o comando 'loc' eu consigo fazer um filtro na Base de Dados
# print(Base_Dados.head())

#Gráfico com a curva de distribuição do valor de vendas
#Tamanho
# plt.figure(figsize=(12, 5))
# #Estilo
# plt.style.use('ggplot')
# #Titulo
# plt.title('Distribuição das Vendas Globais', loc='left', fontsize=14)
# #plot
# sns.kdeplot(Base_Dados['Global'], shade=True, bw=1, color='#96a8a8', linewidth=2.5)
#O comando 'shade' é a sobra dentro da linha, 'bw' afeta a suavização do gráfico de densidade e o 'linewidth' é para a largura da linha
# plt.show()

#Com esse gráfico podemos verificar que existem muitos outliners

#TODO: Criando gráfico(boxplot) para análise da distribuição Global dos games

#Gráfico de análise da distribuição Global dos games
#Tamanho
# plt.figure(figsize=(10,4))
# #Titulo
# plt.title('Análise da distribuição Global  (mi)')
# sns.boxplot(data=Base_Dados, x='Year', y='Global')
# plt.show()
#Podemos ver que tem bastante outliers. O principal outliers dessa base seria o GTA V no ano de 2014

# print(Base_Dados.loc[Base_Dados['Global'] >= 10])
#Com esse print podemos ver os jogos mais vendidos da história do PS4 até 2018, sendo o GTA V o mais vendido
#
#
#TODO: Análisando as porcentagens de venda de cada continente/pais e ano
# e criando um gráfico de barras impilhadas com as porcentagem de cada continente e ano

#Somando todas as vendas dos anos e colocando a tabela 'Year' como index
Analise = Base_Dados.groupby( by=['Year'] ).sum().reset_index()
#print(Analise)
#Criando uma lista com as porcentagens de venda dos Continentes/Pais
#Analisando a proporção dos 100% de cada continente comparado ao Total(Global)
America = [America / Total * 100 for America, Total in zip( Analise['North America'], Analise['Global'] ) ]
Europa = [Europa / Total * 100 for Europa, Total in zip( Analise['Europe'], Analise['Global'] ) ]
Japao = [Japao / Total * 100 for Japao, Total in zip( Analise['Japan'], Analise['Global'] ) ]
Mundo = [Mundo / Total * 100 for Mundo, Total in zip( Analise['Rest of World'], Analise['Global'] ) ]
#
# #Printando as porcentagem de vendas por cada continente
# def Porcentagem(Continente):
#     for porcentagem in Continente:
#         print(porcentagem)
# print('America:',Porcentagem(America))#Não achei um jeito melhor para separar as colunas
# print('Europa:',Porcentagem(Europa))#Esses prints vão vim sempre acompanhados de um None, pois temos um print na função mostrando as porcentagens e esse print que chama a função fica 'sobrando'
# print('Japão:',Porcentagem(Japao))
# print('Mundo:',Porcentagem(Mundo))
#
#
#Aula 6
#Criando um gráfico de barras impilhadas com as porcentagem de cada continente
#Tamnho
# plt.figure(figsize=(10,8))
#Largura da barra no gráfico
Lagura_Barra = 0.85
Rotulo = Analise['Year']
Grupos = [0,1,2,3,4,5]

# #Titulo
# plt.title('Análise distribuição por continente')
#
# #Plt America
# plt.bar(Grupos, America, width=Lagura_Barra, color='#96a8a8', edgecolor='white')
# #Plt Europa
# plt.bar(Grupos, Europa, bottom=America, width=Lagura_Barra, color='#0b3486', edgecolor='white')
# #Plt Japão
# plt.bar(Grupos, Japao, bottom=[A + B for A, B in zip(America, Europa)], width=Lagura_Barra, color='#dd3a76', edgecolor='white')
# #Plt Resto do Mundo
# plt.bar(Grupos, Mundo, bottom=[A + B + C for A, B, C in zip(America, Europa, Japao)], width=Lagura_Barra, color='#e57a18', edgecolor='white')

# #Labels
# plt.xticks(Grupos, Rotulo)
# plt.xlabel('Ano')
# plt.ylabel('Distribuição %')
# plt.legend( [ 'America do Norte', 'Europa', 'Japão', 'Mundo' ], loc='upper left', bbox_to_anchor=(0.15, -0.1), ncol=4 )
# plt.show()


#TODO: Transformando os valores das colunas Publisher, Genre e Game para valores numericos
# Criando as colunas Produtor, Genero e Jogo.
# E criando gráficos para análisar cada uma delas

# print(Base_Dados['Publisher'].unique())

#Transformando os valores das colunas Publisher, Genre e Game para valores numericos
#E criando novas colunas
from sklearn.preprocessing import LabelEncoder

Funcao_Label = LabelEncoder()

Base_Dados['Produtor'] = Funcao_Label.fit_transform( Base_Dados['Publisher'] )
Base_Dados['Genero'] = Funcao_Label.fit_transform( Base_Dados['Genre'] )
Base_Dados['Jogo'] = Funcao_Label.fit_transform( Base_Dados['Game'] )
# print(Base_Dados.head())

#Aula 8
# #Gráfico para análisar as produtoras que mais vendeu nesses anos
# Paleta_Cores = sns.color_palette('husl', 8)
# plt.figure(figsize=(17, 5) )
# plt.title('Análise dos Produtores de Games (mi)')
# sns.scatterplot(data=Base_Dados, x='Produtor', y='Global', color=Paleta_Cores[0] )
# plt.show()


# #Gráfico para análisar os generos mais vendidos nesses anos
# Paleta_Cores = sns.color_palette('husl', 8)
# plt.figure(figsize=(17, 5) )
# plt.title('Análise dos Generos de Games (mi)')
# sns.scatterplot(data=Base_Dados, x='Genero', y='Global', color=Paleta_Cores[0] )
# plt.show()


# #Gráfico para análisar os jogos mais vendidos nesses anos
# Paleta_Cores = sns.color_palette('husl', 8)
# plt.figure(figsize=(17, 5) )
# plt.title('Análise dos Games (mi)')
# sns.scatterplot(data=Base_Dados, x='Jogo', y='Global', color=Paleta_Cores[0] )
# plt.show()

#TODO: ######### Relatorio #########

#Relatorio --> Report para o chefe

# Tamanho da imagem
fig, ax = plt.subplots( figsize=(20, 17) )

#Cor de fundo
Cor_Fundo = '#f5f5f5'
ax.set_facecolor( Cor_Fundo )
fig.set_facecolor( Cor_Fundo )

#Estilo dos gráficos
plt.style.use('seaborn-v0_8-darkgrid')



#Titulo da figura
plt.suptitle('Python para análise de Dados \n Projeto prático 5 - Análise de Mercado de Games PS4', fontsize=22, color='#404040', fontweight=600)


#Parametros para o grid
Linhas = 3
Colunas = 2

# Acessando o gráfico 1
plt.subplot( Linhas, Colunas, 1)
plt.title('Quantidade de Vendas Globais (mi)', fontsize=14)
plt.bar(Base_Dados['Year'], Base_Dados['Global'], color='#69b3a2')
plt.ylabel('Quantidade de Vendas (mi)')

# Acessando o gráfico 2
plt.subplot( Linhas, Colunas, 2)
plt.title('Análise da distribuição Global  (mi)', fontsize=14)
sns.boxplot(data=Base_Dados, x='Year', y='Global')


# Acessando o gráfico 3
plt.subplot( Linhas, Colunas, 3 )
#Largura da barra no gráfico
Lagura_Barra = 0.85
Rotulo = Analise['Year']
Grupos = [0,1,2,3,4,5]
# #Titulo
plt.title('Análise distribuição por continente', fontsize=14)
#Plt America
plt.bar(Grupos, America, width=Lagura_Barra, color='#96a8a8', edgecolor='white')
#Plt Europa
plt.bar(Grupos, Europa, bottom=America, width=Lagura_Barra, color='#0b3486', edgecolor='white')
#Plt Japão
plt.bar(Grupos, Japao, bottom=[A + B for A, B in zip(America, Europa)], width=Lagura_Barra, color='#dd3a76', edgecolor='white')
#Plt Resto do Mundo
plt.bar(Grupos, Mundo, bottom=[A + B + C for A, B, C in zip(America, Europa, Japao)], width=Lagura_Barra, color='#e57a18', edgecolor='white')

#Labels
plt.xticks(Grupos, Rotulo)
plt.xlabel('Ano')
plt.ylabel('Distribuição %')
plt.legend( [ 'America do Norte', 'Europa', 'Japão', 'Mundo' ], loc='upper left', bbox_to_anchor=(0.15, -0.1), ncol=4 )


# Acessando o gráfico 4
plt.subplot( Linhas, Colunas, 4 )
Paleta_Cores = sns.color_palette('husl', 8)
plt.title('Análise dos Produtores de Games (mi)', fontsize=14)
sns.scatterplot(data=Base_Dados, x='Produtor', y='Global', color=Paleta_Cores[0] )


# Acessando o gráfico 5
plt.subplot( Linhas, Colunas, 5 )
Paleta_Cores = sns.color_palette('husl', 8)
plt.title('Análise dos Generos de Games (mi)', fontsize=14)
sns.scatterplot(data=Base_Dados, x='Genero', y='Global', color=Paleta_Cores[0] )


# Acessando o gráfico 6
plt.subplot( Linhas, Colunas, 6 )
Paleta_Cores = sns.color_palette('husl', 8)
plt.title('Análise dos Games (mi)', fontsize=14)
sns.scatterplot(data=Base_Dados, x='Jogo', y='Global', color=Paleta_Cores[0] )


# Ajustar o layout
plt.subplots_adjust( hspace=0.50, wspace=0.15)

# Rodapé
Rodape = '''
Essse relatório foi elaborado no treinado "Python para Análise de Dados"
Está dispónivel no canal do youtube @Data Viking
by: @Rubens Collin
'''

#incluindo o rodapé no relatorio
fig.text(0.5, 0, Rodape, ha='center', va='bottom', size=12, color='#938ca1')

plt.show()