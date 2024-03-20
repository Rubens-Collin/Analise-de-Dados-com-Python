#TODO: Analisando o mercado de Bitcoins da data 24/03/2017 a 28/02/2022

import numpy as np
import pandas as pd


import plotly.express as px
import plotly.graph_objects as Dash

# Lendo a Base de Dados
Base_Dados = pd.read_excel('Dados_Bitcoin.xlsx')

# Verificando
print(Base_Dados.head(10))

# Setar o Index
Base_Dados.set_index('Date', inplace=True)

# Gráfico de Linhas com a coluna 'Close'
fig = px.line(Base_Dados, y='Close')
fig.show()



# Gerar médias moveis
Media_Movel = Base_Dados['Close'].rolling(5).mean()#Pegando a média de 5 período
Media_Tendencia = Base_Dados['Close'].rolling(30).mean() #Pegando a média de 30 período

print(Media_Movel)

# Criando o Dashboard
Figure = Dash.Figure()

# Adicionando o primeiro eixo
#Esse gráfico é igual ao da linha 18, a grande diferença é que podemos customizar muito mais ele com a biblioteca Dash
Figure.add_trace(
    Dash.Scatter(
        x=Base_Dados.index, #Passando o index setado lá na linha 15(nesse caso 'Date')
        y= Base_Dados.Close,
        mode = 'lines', # Defenindo o tipo do gráfico
        name= 'Fechamento',
        marker_color = '#FFA500',
        opacity = 0.5
    )
)

# Adicionando a média móvel. Segundo eixo
Figure.add_trace(
    Dash.Scatter(
        x=Base_Dados.index,
        y= Media_Movel,
        mode = 'lines',
        name= 'Média Móvel',
        marker_color = '#0000FF',
        opacity = 0.5
    )
)

# Adicionando a média tendência. Terceiro eixo
Figure.add_trace(
    Dash.Scatter(
        x=Base_Dados.index,
        y= Media_Tendencia,
        mode = 'lines',
        name= 'Média Tendência',
        marker_color = '#FF1493'
    )
)
#Ajuste no Layout
Figure.update_layout(
    # Titulo
    title = 'Análise do fechamento do Bitcoin',
    #Tamanho
    titlefont_size=20,

    #Ajustando eixo x
    xaxis = dict(
        title='Período Histórico',
        titlefont_size = 20,
        tickfont_size = 20
    ),
    #Ajustando eixo y
    yaxis = dict(
        title='Preço de fechamento ($)',
        titlefont_size = 20,
        tickfont_size = 20
    ),

    # Parametros para a Legenda
    legend = dict(
        font_size = 20,
        y=1, #Com os parametros y e x eu posso mudar a posição da minha legenda(a legenda é o nome do meus eixos)
        x=1,
        bgcolor='rgba(255, 255, 255, 1)', #Eu mudo a cor de fundo da minha legenda
    )

)
Figure.show()
