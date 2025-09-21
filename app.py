import pandas as pd
import glob

csv_files = glob.glob('assets/*.csv')

df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
df = df[df['product'].str.lower() == 'pink morsel']

df['sales'] = df['price'] * df['quantity']
df = df[['date', 'region', 'sales']]

df.to_csv('assets/daily_sales_data_pinkMorsel.csv', index=False)

import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
import plotly.express as px

fig = px.line(df,x='date',y='sales',title='pink morsel sales')

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Pink Morsel Sales Visualizer"),
    dcc.Graph(figure=fig)
], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
