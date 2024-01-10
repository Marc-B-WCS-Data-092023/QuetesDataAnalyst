from dash import Dash, dcc, html, Output, Input
import pandas as pd 
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', on_bad_lines = 'skip')
df = df.sort_values(by=['  num_pages'], ascending = False)

#fig = px.bar(df.head(10), x="title", y="  num_pages", height=800)

# Layout de base
app.layout = html.Div([
    html.H1("Challenge Dash Livres", style={'textAlign': 'center', 'color': 'blue'}),
    dcc.Dropdown(df['authors'].unique(), placeholder = 'Auteur', id='liste'),
    dcc.Slider(
        id='slider',
        min=df['  num_pages'].min(),
        max=df['  num_pages'].max(),
        value=df['  num_pages'].max(),
        step=100,
        marks={i: str(i) for i in range(0, 8000, 200)}  # Marques sur le curseur
    ),
    dcc.Graph(id='graph1', className='graph-style')
])

@app.callback(
    Output('graph1', 'figure'),
    [Input('liste', 'value')],
    [Input('slider', 'value')]
)
def update_graph(value, value2):
    data_filtered = df[df['authors'] == value]
    data_filtered = data_filtered[data_filtered['  num_pages'] <= value2]
    data_filtered = data_filtered.sort_values(by=['  num_pages'], ascending = False)
    fig = px.bar(data_filtered, x="title", y="  num_pages", height=800)
    fig.update_layout(title=f"Livres de {value}", xaxis_title='Nombre de pages', yaxis_title='Titre')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
