#TODO: Análisando as porcentagens de venda de cada continente/pais e ano
# e criando um gráfico de barras impilhadas com as porcentagem de cada continente e ano

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

#Somando todas as vendas dos anos e colocando a tabela 'Year' como index
Analise = Base_Dados.groupby( by=['Year'] ).sum().reset_index()
print(Analise)
#Criando uma lista com as porcentagens de venda dos Continentes/Pais
#Analisando a proporção dos 100% de cada continente comparado ao Total(Global)
America = [America / Total * 100 for America, Total in zip( Analise['North America'], Analise['Global'] ) ]
Europa = [Europa / Total * 100 for Europa, Total in zip( Analise['Europe'], Analise['Global'] ) ]
Japao = [Japao / Total * 100 for Japao, Total in zip( Analise['Japan'], Analise['Global'] ) ]
Mundo = [Mundo / Total * 100 for Mundo, Total in zip( Analise['Rest of World'], Analise['Global'] ) ]

#Printando as porcentagem de vendas por cada continente
def Porcentagem(Continente):
    for porcentagem in Continente:
        print(porcentagem)
print('America:',Porcentagem(America))#Não achei um jeito melhor para separar as colunas
print('Europa:',Porcentagem(Europa))#Esses prints vão vim sempre acompanhados de um None, pois temos um print na função mostrando as porcentagens e esse print que chama a função fica 'sobrando'
print('Japão:',Porcentagem(Japao))
print('Mundo:',Porcentagem(Mundo))

#Criando um gráfico de barras impilhadas com as porcentagem de cada continente
#Tamnho
plt.figure(figsize=(10,8))
#Largura da barra no gráfico
Lagura_Barra = 0.85
Rotulo = Analise['Year']
Grupos = [0,1,2,3,4,5]

#Titulo
plt.title('Análise distribuição por continente')

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

plt.show()
