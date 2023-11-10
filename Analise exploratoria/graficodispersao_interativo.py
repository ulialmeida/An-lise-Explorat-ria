import plotly.express as px    #para aparecer o nome de forma interativa
import pandas as pd

# Abrir o arquivo CSV com o delimitador ';;'
df = pd.read_csv('/content/molecular_cpnd_bd.csv', delimiter=';')
df = df.drop(columns=['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])

fig = px.scatter(df, x='molecular_formula', y='molecular__mass', hover_name='compound')

# Personaliza o layout
fig.update_layout(
    title='Gráfico de Dispersão com Hover',
    xaxis_title='Fórmula Molecular',
    yaxis_title='Massa Molecular'
)

# Personaliza as informações de hover
fig.update_traces(textposition='top center')

fig.show()
fig.show()
