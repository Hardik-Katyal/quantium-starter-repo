import pandas as pd
import glob

# --- Data prep ---

def cleaned(df):
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    df = df[df['product'].str.lower() == 'pink morsel']
    df['sales'] = df['price'] * df['quantity']
    df = df[['date', 'region', 'sales']]
    return df

def exportcsv(df):
    df.to_csv('assets/pinkMorsel.csv', index=False)

#Dash app
import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
import plotly.express as px

def create_dash_app(df):
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

    app.layout = dbc.Container([
        html.H1("Pink Morsel Sales Visualizer",
                id='main-header',
                className="text-center text-primary mb-4"),

        # Region selector
        dcc.RadioItems(
            id='region-radio',
            options=[{'label': r, 'value': r} for r in df['region'].unique()],
            value=df['region'].unique()[0],  # default
            inline=True
        ),

        dcc.Graph(id='sales-graph')
    ], fluid=True)

    # Callback
    @app.callback(
        Output('sales-graph', 'figure'),
        Input('region-radio', 'value')
    )
    def update_graph(selected_region):
        filtered_df = df[df['region'] == selected_region]
        fig = px.line(
            filtered_df, x='date', y='sales',
            title=f"Pink Morsel Sales in {selected_region}",
            markers=True
        )
        fig.update_layout(template="plotly_white")
        return fig
    return app

def run_dash_app(df):
    app = create_dash_app(df)
    app.run(debug=True)


if __name__ == "__main__":
    csv_files = glob.glob('assets/*.csv')
    df = cleaned(pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True))
    exportcsv(df)

    # Reload and sort
    df = pd.read_csv('assets/pinkMorsel.csv').sort_values(by='date')

    run_dash_app(df)