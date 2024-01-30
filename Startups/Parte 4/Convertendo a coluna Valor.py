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
print('Coluna Valor com o dtype: object\n',Base_Dados['Valor ($)'].head(),'\n\n')

#Convertendo a coluna Valor
#TODO: apply é uma função do Pandas onde eu consigo mexer dentro da miha coluna,
# percorrendo linha por linha e fazer algum tipo de opreração.
Base_Dados['Valor ($)'] = pd.to_numeric(Base_Dados['Valor ($)'].apply(lambda Linha:
                                                        Linha.replace('$', '')))
print('Coluna Valor com o dtype: float64\n',Base_Dados['Valor ($)'].head(),'\n\n')

# Tabela Anlitica
# A função groupby ela agrupa as informações selecionadas
Analise_Pais = Base_Dados.groupby(by=['Pais'])['Valor ($)'].sum().reset_index()
print(Analise_Pais.head(),'\n\n')

Analise_Valor = Analise_Pais.sort_values('Valor ($)', ascending=False)#com a 'função sort_values' eu ordenei os valores e com o comando 'ascending=False' com esse comando eu ordenei do maior para o menor
print(Analise_Valor)
plt.figure(figsize=(15, 8))
plt.plot(Analise_Valor['Pais'], Analise_Valor['Valor ($)'])
plt.title('Analise do Valor por Pais')
plt.xticks(rotation=40, ha='right')
plt.show()