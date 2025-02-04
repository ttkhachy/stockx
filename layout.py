from dash import dcc, html

def create_layout():
    return html.Div([
    html.Div([
        html.H1("Finance Portfolio Dashboard"),
        html.P("Search and analyze stock market trends with ease."),
    ]),
    html.Div([
        html.Label("Select Period:"),
        dcc.Dropdown(id="period",
                        options=[
                            {"label": "5 Days", "value": "5d"},
                            {"label": "1 Month", "value": "1mo"},
                            {"label": "3 Months", "value": "3mo"},
                            {"label": "6 Months", "value": "6mo"},
                            {"label": "1 Year", "value": "1y"},
                            {"label": "Year to Date", "value": "ytd"},
                            {"label": "Max", "value": "max"},
                        ],
                        value="5d",
                        multi=False,
                        style={"width": "40%"}

        ),
        html.Label("Enter Stock Ticker:"),
        dcc.Input(id="ticker_input", type="text", placeholder="AAPL", style={'marginRight':'10px'})
    ], style={"width": "30%", "float": "left", "padding": "20px"}),

    html.Div([
        html.Div(id="current_price", children=[]),
        dcc.Graph(id="stock_graph", figure={}),
    ], style={"width": "65%", "float": "left", "padding": "20px"}),

    html.Div([
        html.Label("Enter stock name and value, then press submit:"),
        dcc.Input(id="stock_name", type="text", placeholder="Enter Stock Name:"),
        dcc.Input(id="stock_amount", type="number", placeholder="Enter Stock Value:"),
        html.Button('Submit', id='submit-val', n_clicks=0),
        ## how can i get this to be below the graph?
    ])
])

