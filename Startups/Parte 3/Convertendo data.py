import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #Com essa biblioteca e essa função tira alguns avisos.

#ler os dados
Base_Dados = pd.read_csv('../Startups in 2021 end.csv')

# Renomer colunas
Base_Dados.rename( columns={
    'Company' : 'Empresa',
    'Valuation ($B)' : 'Valor ($)',
    'Date Joined' : 'Data de Adesão',
    'Country' : 'Pais',
    'City' : 'Cidade',
    'Industry' : 'Setor',
    'Investors' : 'Investidores'
}, inplace=True) # Com esse parametro 'inplace=True' eu aplico essas mudanças na Base de dados


#Conversão para Data
print('Coluna Data com o dtype: object\n',Base_Dados['Data de Adesão'],'\n\n')

#Conversão da coluna 'Data de Adesão' para data
Base_Dados['Data de Adesão'] = pd.to_datetime(Base_Dados['Data de Adesão'])
print('Coluna Data com o dtype: datetime\n',Base_Dados['Data de Adesão'].head(),'\n\n')

#Extrair ano, mes e dia
Base_Dados['Mes'] = pd.DatetimeIndex(Base_Dados['Data de Adesão']).month
Base_Dados['Ano'] = pd.DatetimeIndex(Base_Dados['Data de Adesão']).year
Base_Dados['Dia'] = pd.DatetimeIndex(Base_Dados['Data de Adesão']).day
#Eu criei uma coluna 'Mes' e extrai o dado da coluna 'Data de Adesão' com o comando .month
print(Base_Dados.head(),'\n\n')

# Tabela Anlitica
# A função groupby ela agrupa as informações selecionadas                                 #A coluna 'Setor' está aqui para que fique melhor na hora do print, sem isso o programa vai printar todas as colunas
Analise_Agrupada = Base_Dados.groupby(by=['Pais', 'Ano', 'Mes', 'Dia', 'Empresa']).count()['Setor'].reset_index()
print(Analise_Agrupada.head(),'\n\n')

#TODO: A função 'loc' localiza alguma coisa na Base de Dados
print('Tabela com as Startups do Brasil:\n\n',Analise_Agrupada.loc[
    Analise_Agrupada['Pais'] == 'Brazil'
])

print(Analise_Agrupada.loc[
    Analise_Agrupada['Pais'] == 'United States'
])
