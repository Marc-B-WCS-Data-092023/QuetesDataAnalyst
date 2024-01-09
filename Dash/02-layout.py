import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

link = 'https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv'

df_books = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', on_bad_lines = 'skip')

print(df_books.head())

fig = px.bar(df_books.head(10), x="title", y="  num_pages", labels={'title':'titre du livre', '  num_pages':'nombre de pages'}, title="Nombre de pages par titre")

# Initialisation de l'application Dash
app = Dash(__name__)

# Layout de l'application Dash
app.layout = html.Div(
    [
        html.H1("Un titre principal pour l'application!"),
        
        # Graphique Plotly Express
        dcc.Graph(figure=fig, id='mon-graph', className='graph-style'),
        
        # Liste déroulante
        dcc.Dropdown(
            options=[{'label': auteur, 'value': auteur} for auteur in df_books['authors']],
            value=df_books['authors'].iloc[0],  # Valeur par défaut
            id='dropdown'
        ),
        
        # Champ de saisie de nombre
        dcc.Input(
            type='number',
            value=150,
            id='input-number'
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)