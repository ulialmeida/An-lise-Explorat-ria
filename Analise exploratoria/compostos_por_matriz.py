import pandas as pd
import matplotlib.pyplot as plt

# Abre o arquivo CSV
df = pd.read_csv('compostos_planilha_inicial.csv')

# Contagem de compostos em cada matriz de extração
counts = df['matrixes_id'].value_counts()

# Para calcular a porcentagem
total_compostos = len(df)
porcentagens = (counts / total_compostos) * 100

# Definir as cores para as barras
cores = ['#0000FF', '#00CED1', '#00FFFF', '#4682B4', '#5F9EA0', '#87CEEB', '#6495ED', '#1E90FF']

plt.figure(figsize=(10, 6))
plt.bar(counts.index, counts.values, color=cores)  # Usar counts.index como 'x' e counts.values como 'y'

# Adicionar porcentagem 
for i, count in enumerate(counts):
    plt.text(counts.index[i], count + 1, f'{porcentagens.iloc[i]:.2f}%', ha='center')

plt.xlabel('Matrizes de Extração')
plt.ylabel('Quantidade de Compostos')
plt.title('Contagem de Compostos por Matriz de Extração')
plt.show()