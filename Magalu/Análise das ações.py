#TODO: Analisando as ações da Magalu do ano de 2021
# Com essa analise podemos ver que as ações da Magalu dispencou dentro de 1 ano
# Com as ações caindo de R$25 para R$7

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

import calendar

import warnings
warnings.filterwarnings('ignore')

#Lendo a Base de Dados
Base_dados = pd.read_excel('Magalu.xlsx')

#Analisando
print(Base_dados.shape)#Verifiacando a dimensão

print(Base_dados.info())#Verifianco os Dtype das colunas


# Seriés Temporais
Dados = Base_dados.set_index('Data')#Colocando a coluna 'Data' como index

#Criando um gráfico para minha série temporal
#print(plt.style.available)# Esse print é para explorar a lista completa de style disponiveil
plt.style.use('seaborn-v0_8-darkgrid')#Modificando a cor do fundo do gráfico
plt.figure(figsize=(16, 5))#Tamanho do gráfico
plt.title('Análises das ações da magalu - Fechamento', fontsize=15, loc='left') #Com o 'loc' eu posiciono o title para a esquerda
plt.plot(Dados.index, Dados['Fechamento'])
plt.xlabel('Período da Cotação')
plt.ylabel('Valor da ação ($)')
plt.show()

#Verificando os primeiros registros da Base
print(Dados.head())
#Verificando os últimos registros da Base
print(Dados.tail())


print(Dados['Fechamento'].rolling(5).mean())#Com a função 'rolling' eu faço uma média movel dos valores, nessa caso foi a coluna fechamento

Media_Movel = Dados['Fechamento'].rolling(5).mean()

Media_Tendencia = Dados['Fechamento'].rolling(30).mean()

#Criando um gráfico com todas as ações mais a média movel de 5 dias e a média movel de 30 dias
plt.style.use('seaborn-v0_8-darkgrid')
plt.figure(figsize=(16, 5))
plt.title('Análises das ações da magalu - Fechamento', fontsize=15, loc='left')
plt.plot(Dados.index, Dados['Fechamento'])
plt.plot(Dados.index, Media_Movel )
plt.plot(Dados.index, Media_Tendencia )

plt.xlabel('Período da Cotação')
plt.ylabel('Valor da ação ($)')
plt.show()

#Criando um boxplot para a Coluna 'Fechamento'
sns.boxplot(data=Dados, x='Fechamento')
plt.show()

#Criando um Boxplot com todos os mês
Base_dados['Mes'] = Base_dados['Data'].dt.month #Criando uma cluna mês na Base de Dados
print(Base_dados.head())
print(Base_dados.tail())
plt.figure(figsize=(16,5))
sns.boxplot(data=Base_dados, x='Mes', y='Fechamento')
plt.show()
#Com esse Gráfico vemos que o mês de Março foi o que mais oscilou e o mês que menos oscilou foi junho

#Fazendo uma nalise completa da coluna 'Fechamento'
print(Base_dados.groupby(['Mes']).describe()['Fechamento'])


# Filtrando os dados dos meses
for mes in range(1, 13):
    # Trocando os números do mes para nomes
    nome_mes = calendar.month_name[mes]
    # Obtendo os dados do mês
    dados_mes = Base_dados[Base_dados['Mes'] == mes]
    # Obtendo a média da coluna 'Fechamento'
    media_mes = dados_mes['Fechamento'].mean()
    print(f'Dados do mês {nome_mes}:\n {dados_mes}\n')
    print(f'A média do mes {nome_mes} é: {media_mes:.2f}\n\n')


#Criando gráfico de mercado de investimento
Grafico = go.Figure(
    data=[
        go.Candlestick(
            x=Dados.index,
            open= Dados['Abertura'],
            high= Dados['Maior'],
            low= Dados['Menor'],
            close= Dados['Fechamento'],
        )
    ]
)

Grafico.update_layout(xaxis_rangeslider_visible=False)

Grafico.show()

