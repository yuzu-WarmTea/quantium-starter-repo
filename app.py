# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

path = "new_data.csv"

# retrieving the data into a list
data = pd.read_csv(path, header=0)
sales = list(data.Sales)
dates = list(data.Date)
regions = list(data.Region)


colors = {
    'background': '#D3C0D2',
    'text': '#DAFFEF',
    'main-bg': '#D0FFD6',
    'title-tx': '#A6979C',
    
}



df = pd.DataFrame({
    "Date": dates,
    "Sales": sales,
    "Regions": regions
})

fig = px.line(df, x="Date", y="Sales", color="Regions")



fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['main-bg']}, children=[
    html.H1(
        children='Soul Foods Visualiser',
        style={
            'textAlign': 'left',
            'color': colors['title-tx']
        }
    ),

    html.Div(children='Here is the visualization of Soul Food sales ordered through date.', style={
        'textAlign': 'left',
        'color': colors['title-tx']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
