#TODO: Nessa parte irei me aprofundar mais nos dados, verificando a porcentagem
# de mulheres e homens... e trabalhando com vários boxplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') #Com essa biblioteca e essa função tira alguns avisos.

#Lendo a Base de Dados
Base_Dados = pd.read_csv('StudentsPerformance+(1).csv')


#Informações da Base
print(Base_Dados.info(),'\n\n')

#Verificando a porcentagem de mulheres e homens na minha Base
print(Base_Dados['gender'].value_counts(normalize=True) * 100,'\n\n') #Com o comando 'normalize=True' eu ordeno do maior para o menor

#Verificando a porcentagem de grupo de raça e etnia
print(Base_Dados['race/ethnicity'].value_counts(normalize=True) * 100,'\n\n')

#Verificando o nível educacional das pessoas.
print(Base_Dados['parental level of education'].value_counts(normalize=True) * 100,'\n\n')

#Almoço? standard? não entendi muito bem
print(Base_Dados['lunch'].value_counts(normalize=True) * 100,'\n\n')

#Verificando se pessoa fez um teste preparatório antes de fazer o teste.
print(Base_Dados['test preparation course'].value_counts(normalize=True) * 100,'\n\n')
#64% das pessoas não fizeram os testes preparatórios antes das provas


#Exibindo um boxplot com as notas de matemática
sns.boxplot( data=Base_Dados, x='math score', y='gender')
plt.show()
#No sexo feminino temos um maior indice de outliers. Os homens tem uma média maior em comparação as mulheres

#Exibindo um boxplot com as notas de leitura
sns.boxplot( data=Base_Dados, x='reading score', y='gender')
plt.show()
#No sexo feminino continuamos a ter um maior indice de outliers, mas também temos a maior média

#Exibindo um boxplot com as notas de redação
sns.boxplot( data=Base_Dados, x='writing score', y='gender')
plt.show()
#No sexo feminino continuamos a ter um maior indice de outliers, mas também temos a maior média

#Descrevendo as notas de matemática pelo genero
print(Base_Dados.groupby(by=['gender']).describe()['math score'].reset_index())
#Esse plot é para ajudar na comparação com o print de cima
sns.boxplot( data=Base_Dados, x='math score', y='gender')
plt.show()


