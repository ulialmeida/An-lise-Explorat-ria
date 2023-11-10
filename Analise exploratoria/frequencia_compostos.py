import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abrir o arquivo CSV 
df = pd.read_csv('compostos_planilha_inicial.csv')

# Definir coluna
coluna_composto = 'compound_id'

# A função 'duplicated' ajuda a encontrr linhas duplicadas na coluna 'compound'
duplicatas = df[df.duplicated(subset=[coluna_composto], keep=False)]

# Criar um dicionário para mapear compostos a cores diferentes
compostos_duplicados = duplicatas[coluna_composto].value_counts()
compostos_mais_de_2_vezes = compostos_duplicados[compostos_duplicados > 2]
paleta_cores = sns.color_palette("Set2", len(compostos_mais_de_2_vezes))

# Criar um mapeamento de composto para cor
mapeamento_composto_cor = {}
for composto, cor in zip(compostos_mais_de_2_vezes.index, paleta_cores):
    mapeamento_composto_cor[composto] = cor

# Atribuição de cores aos compostos no gráfico de barras
plt.figure(figsize=(10, 6))
compostos_duplicados.plot(kind='bar', color=[mapeamento_composto_cor.get(comp, 'blue') for comp in compostos_duplicados.index])
plt.xlabel('ID composto')
plt.ylabel('Número de Repetições')
plt.title('Compostos Mais Frequentes')
plt.xticks(rotation=90)
plt.show()