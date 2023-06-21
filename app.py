
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

path = "new_data.csv"

# retrieving the data into a list
data = pd.read_csv(path, header=0)
data = data.sort_values(by="Date")
sales = list(data.Sales)
dates = list(data.Date)
regions = list(data.Region)



colors = {
    'background-dark': '#333533',
    'background-light1': '#CFDBD5',
    'background-light2': '#E8EDDF',
    'text': '#DAFFEF',
    'main-bg': '#D0FFD6',
    'title-tx': '#A6979C',
    'graph-bg': '#F5CB5C',
    'graph-tx': '#242423'
}

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales,
    "Regions": regions,
})

reg = ['North', 'East', 'South', 'West']

fig = px.line(df, x="Date", y="Sales", color="Regions")



fig.update_layout(
    plot_bgcolor=colors['graph-bg'],
    paper_bgcolor=colors['graph-bg'],
    font_color=colors['graph-tx']
)





# App layout and styling

app.layout = html.Div([
    html.Div(
        className = "app-header",
        children = [
            html.Div('Soul Foods', className = "app-header--title")
        ]
    ),
    html.Div(
        children = html.Div([
            html.H3('Overview'),
            html.P(''' Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus interdum pulvinar dui. Etiam vel est porta, viverra orci non, consectetur metus. Pellentesque ornare vitae urna vitae ultrices. Vivamus fermentum mi non turpis vulputate venenatis.
                    Mauris suscipit suscipit vestibulum. Etiam sagittis dolor eros, at pulvinar nisl porttitor quis. Nullam consectetur lacinia purus eget tincidunt. Donec consequat nisl quis eros rhoncus eleifend. Nam sed risus ut ipsum condimentum laoreet ac ac neque. Donec sit amet porttitor urna, eu ullamcorper nulla. 
                    Aenean consectetur magna ac nibh fermentum sagittis. Suspendisse egestas accumsan purus quis mollis. Quisque molestie venenatis orci quis sollicitudin.
            ''')
        ])
    ),
    dcc.Graph(
        id='line-graph-sales',
        figure = fig,
        className = "graph-line"
    ),
    dcc.RadioItems([
        {'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'}
    ], inline = True, id = 'region-radio')

])

if __name__ == '__main__':
    app.run_server(debug=True)


@app.callback(
    Output('line-graph-sales','figure'),
    Input('region-radio', 'value') 
)
def update_figure(selected_region):
    filtered_df = df[df['Regions'] == selected_region]

    fig = px.line(filtered_df, x = "Date", y = "Sales", colors = "Regions")

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig