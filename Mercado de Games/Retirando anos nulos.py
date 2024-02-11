#TODO: Retirando os anos nulos(2019 e 2020) da minha Base de Dados
# Criando um gráfico com a curva de distribuição do valor de vendas

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
#Com o comando 'loc' eu consigo fazer um filtro na Base de Dados
print(Base_Dados.head())

#Gráfico com a curva de distribuição do valor de vendas
#Tamanho
plt.figure(figsize=(12, 5))
#Estilo
plt.style.use('ggplot')
#Titulo
plt.title('Distribuição das Vendas Globais', loc='left', fontsize=14)
#plot
sns.kdeplot(Base_Dados['Global'], shade=True, bw=1, color='#96a8a8', linewidth=2.5)
#O comando 'shade' é a sobra dentro da linha, 'bw' afeta a suavização do gráfico de densidade e o 'linewidth' é para a largura da linha
plt.show()

#Com esse gráfico podemos verificar que existem muitos outliners

