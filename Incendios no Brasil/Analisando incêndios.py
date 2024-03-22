#TODO: Fazendo uma série de gráficos e mapa de calor, com a base de dados de Incêncidios no Brasil de 1998 a 2017

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# Lendo os dados
Base_Dados = pd.read_csv('Dados_Incendio.csv', encoding='latin-1')

# Verificando
print(Base_Dados.head())

# Verificando campos nulos
print(Base_Dados.isnull().sum())

# Nulos Plot
plt.figure(figsize=(15, 7))
plt.title('Análise de campos nulos')
sns.heatmap(Base_Dados.isnull(), cbar=False)
plt.show()

# Estatiticas
print(Base_Dados.describe())

# Infos
print(Base_Dados.info())


# Campos únicos
print(Base_Dados.nunique())


# Análise por anos dos incendios
Analise_anos = Base_Dados.groupby(by=['year']).sum().reset_index()[['year', 'number']] #Com esse comando '[[]]' eu consigo printar apenas as colunas que eu quero
print(Analise_anos)

# Tamanho
plt.figure(figsize=(12, 5))

# Style
plt.style.use('ggplot')

# Gráfico
plt.title(  'Total de incêndios no Brasil: 1997 a 2017', loc='left', fontsize=14)
sns.lineplot(data = Analise_anos, x='year', y='number', estimator='sum', lw=2, color='#FF0000', alpha=0.85)

# Labels
plt.xlabel('Quantidade')
plt.ylabel('Período')
plt.show()

# Análise por meses dos incendios
Analise_mes = Base_Dados.groupby(by=['year', 'month']).sum().reset_index()[['year', 'month', 'number']]
print(Analise_mes)

# Tamanho
plt.figure(figsize=(12, 5))

# Gráfico e ordenação dos meses
plt.title('Total de incêndios no Brasil: Meses', loc='left', fontsize=14)
sns.boxplot(data=Analise_mes, x='month', y='number', palette='coolwarm', saturation=1, width=0.9, linewidth=2,
            order=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
                   'Setembro', 'Outubro', 'Novembro', 'Dezembro'])

# Labels
plt.xlabel('Mês')
plt.ylabel('Número de incêndios')
plt.show()


# Análise por estados
Analise_estado = Base_Dados.groupby(by=['state']).sum().reset_index()[['state', 'number']].sort_values('number', ascending=False) #.sort_values('number', ascending=False) fazendo isso eu deixo em ordem crescente
print(Analise_estado.head(),'\n')

# Tamanho
plt.figure(figsize=(12, 8))

# Título
plt.title('Estados com os maiores números de incêndios', loc='left', fontsize=14)

# Gráfico por Estado
plt.bar(Analise_estado.state, Analise_estado['number'], color='#FF0000') #Aqui eu mostro dois tipos de como podemos chamar uma coluna do nosso Banco. Pode ser pelo '.' ou o '['']'

# Labels
plt.ylabel('Quantidade')
#Colocando os nomes dos estados em 90° para que fique melhor a visualização
plt.xticks(rotation=90)
plt.show()



# Separando os 10 estados com o maior números de incêndios
print(Analise_estado.state[0:10])
# Colocando os 10 estados em uma variavel
Lista_TOP10 = Analise_estado.state[0:10].values

# Tamanho
plt.figure(figsize=(14, 5))

# Título
plt.title('Top 10 Estados com incêndios', loc='left' ,fontsize= 14)

# Loop
for Coluna in Lista_TOP10:
    # Filtrar o Estado
    Filtro = Base_Dados.loc[Base_Dados['state'] == Coluna]

    # Agrupando os valores para sumarizar
    Analise_Local = Filtro.groupby(by=['year']).sum().reset_index()

    # plot
    sns.lineplot(data=Analise_Local, x='year', y='number', lw=2, alpha=0.85)

# Labels
plt.xlabel('Período')
plt.ylabel('Quantidade')

# Legenda
plt.legend(Lista_TOP10, bbox_to_anchor=(1,0.7)) # Eu uso o comando 'bbox_to_anchor' para posicionar a minha legenda no plot (x, y)
plt.show()


# Plot Geográfico

# Gerando os estados
Estados = Analise_estado.sort_values('state')['state'].values

# Gerando os valores
Valores = Analise_estado.sort_values('state')['number'].values

# Latitudes
Lat = [ -8.77, -9.71,	1.41, -3.07,	-12.96, -3.71, -15.83, -19.19, -16.64, -2.55,	-12.64,
       -18.10, -7.06, -5.53, -8.28, -8.28,	-22.84,	-11.22,	1.89,	-27.33,	-23.55,	-10.90,	-10.25 ]

# Longitudes
Log = [ -70.55,	-35.73,	-51.77,	-61.66,	-38.51,	-38.54,	-47.86,	-40.34,	-49.31,	-44.30,	-55.42,	-44.38,
       -35.55,	-52.29,	-35.07,	-43.68,	-43.15,	-62.80,	-61.22,	-49.44,	-46.64,	-37.07,	-48.25 ]

# Organizando os dados
Dicionario = {
    'Estado' : Estados,
    'Latitude' : Lat,
    'Longitude' : Log,
    'Incêndios' : Valores
}

# Lendo o dicionario
Analise_Geografica = pd.DataFrame (Dicionario)

print(Analise_Geografica.head())

# Fazendo o Plot
# Importando a biblioteca para fazermos o mapa de calor geográfico
import plotly.express as px

# Mapa de Calor Geográfico
fig = px.density_mapbox(
    Analise_Geografica,
    lat='Latitude',
    lon='Longitude',
    z='Incêndios',
    radius=30,
    center=dict(lat=-12.700, lon=-46.5555),
    zoom=3,
    mapbox_style='stamen-terrain'
)
fig.show()