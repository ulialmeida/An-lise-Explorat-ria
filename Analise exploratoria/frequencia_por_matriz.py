import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Abra o arquivo CSV (certifique-se de que seu DataFrame esteja carregado corretamente)
df = pd.read_csv('compostos_planilha_inicial.csv')

# Escolha a coluna que você deseja verificar para duplicatas, por exemplo, 'compound'
coluna_composto = 'compound_id'

# Use a função 'duplicated' para encontrar linhas duplicadas com base na coluna 'compound'
duplicatas = df[df.duplicated(subset=[coluna_composto], keep=False)]

# Defina 'matrixes_id' como índice
duplicatas = duplicatas.set_index('matrixes_id')

# Agrupe as duplicatas por 'matrixes_id' e conte a contagem de duplicatas em cada matriz
compostos_duplicados_por_matriz = duplicatas.groupby(['matrixes_id', coluna_composto]).size().unstack(fill_value=0)

# Use a paleta de cores "tab20" para diferenciar as matrizes
paleta_cores = sns.color_palette("tab20", len(compostos_duplicados_por_matriz.columns))

# Crie o gráfico de barras empilhado
plt.figure(figsize=(12, 6))
compostos_duplicados_por_matriz.plot(kind='bar', stacked=True, color=paleta_cores)
plt.xlabel('Matriz de Extração')
plt.ylabel('Contagem de Frequencia')
plt.title('Compostos Frequentes por Matriz de Extração')
plt.legend(title='Composto', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.xticks(rotation=45)
plt.show()