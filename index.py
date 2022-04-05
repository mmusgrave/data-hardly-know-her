# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
# from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from app import app, server
from tabs import trade, methodology, evaluate


style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('### NFL Fantasy Football Trade Analyzer'),
    dcc.Tabs(id='tabs', value='tab-trade', children=[
        dcc.Tab(label='Trade', value='tab-trade'),
        dcc.Tab(label='Methodology', value='tab-methodology'),
        dcc.Tab(label='Evaluate', value='tab-evaluate'),
    ]),
    html.Div(id='tabs-content'),
], style=style)


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-trade': return trade.layout
    elif tab == 'tab-methodology': return methodology.layout
    elif tab == 'tab-evaluate': return evaluate.layout


if __name__ == '__main__':
    app.run_server(debug=True)
