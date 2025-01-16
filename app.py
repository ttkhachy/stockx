import streamlit as st
import yfinance as yf
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash()

app.layout = html.Div([
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
    ], style={"width": "65%", "float": "right", "padding": "20px"}),
])

@app.callback(
    [Output(component_id="current_price", component_property="children"),
        Output(component_id="stock_graph", component_property="figure")],
    [Input(component_id="period", component_property="value"),
    Input(component_id="ticker_input", component_property="value"),]
)
def update_graph(period_slct, ticker_input):
    print(period_slct)
    print(ticker_input)

    try:
        ticker = yf.Ticker(ticker_input)
        current_price = ticker.info["currentPrice"]
        
    except:
        current_price = "Error: Please enter a valid ticker"

    df = ticker.history(period=period_slct)
    fig = px.line(df,
                  y="Close",
                  template="plotly_white")

    return current_price, fig

if __name__ == "__main__":
    ticket = yf.Ticker("AAPL")
    print(ticket.info["currentPrice"])

    app.run_server(debug=True)
 