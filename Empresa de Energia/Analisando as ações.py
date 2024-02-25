#TODO: Analisando as ações das empresa de energia

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#Lib para ignorar avisos
import warnings
#Desabilitando avisos
warnings.filterwarnings('ignore')

#Lendo a Base de Dados
Base_Dados = pd.read_excel('Dados_Empresas_Energia.xlsx')

# Verificando
print(Base_Dados.head())


# Serie Temporais -  Setar o Index
Base_Dados.set_index('Data', inplace=True)
print(Base_Dados.head())

#Gráfico

#Estilo do gráfico
plt.style.use('seaborn-v0_8-darkgrid')

#Tamanho
plt.figure( figsize=(16, 7) )

#Título
plt.title('Análise de ações de empresas de Energia', loc='left', fontsize=18, fontweight=0 )

# Plot da Petrobras
plt.plot(Base_Dados.index, Base_Dados['Petrobras'], color='#008000', linewidth=4, alpha=0.7)#Com o alpha eu deixo a cor mais opaca

#Texto da Petrobras
plt.text(Base_Dados.index[-1], Base_Dados['Petrobras'].tail(1), 'Petobras', color='#008000', size='large', horizontalalignment='left')
#Outra forma de colocar um texto
plt.legend( ['Petrobras'], loc='upper left', bbox_to_anchor=(0.15, -0.1))

#Labels
plt.xlabel('Período')
plt.ylabel('Preço de Fechamento (R$)')

#Plot de todas as colunas
for Coluna in Base_Dados.columns[1:]: #com o comando '[1:]' eu tiro a coluna Petrobras do For

    #Plot da Alupar(Com esse if eu mostro como mudar a cor de cada ação)
    if Coluna == 'Alupar':
        plt.plot(Base_Dados.index, Base_Dados['Alupar'], color='blue', linewidth=4, alpha=0.7)
        # Texto da Alupar
        plt.text(Base_Dados.index[-1], Base_Dados['Alupar'].tail(1), 'Alupar', color='blue', size='large',
                 horizontalalignment='left')

    else:#Precisa desse Else? Fiz sem ele e deu certo também
        #Plot das outras ações
        plt.plot(Base_Dados.index, Base_Dados[Coluna], color='gray', linewidth=4, alpha=0.2)
        #Texto das outras ações
        plt.text(Base_Dados.index[-1], Base_Dados[Coluna].tail(1), Coluna, color='gray', size='large',
                 horizontalalignment='left')

plt.show()

#TODO: Podemos ver que as ações dessas empresas de energia oscila bastante