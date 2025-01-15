import streamlit as st
import yfinance as yf
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

 # app = dash.Dash(__name__)

## idea - depending on how each getter method is formatted within yfin - e.g dividends etc - maybe can make a function for each
#getter and then do pandas stuff and return it in the desired way so that all of them are consistant for the plotly stuff?
app = Dash()
## so the yfinance thing is directly connected to yahoo finance. so the names of the 

#ticker_symbol = input("please enter the name of the ticker to be searched: ")
ticker_symbol = "AAPL"

# can just get normal user input and then if the output of yfin ticker getter is none then can display an error message in the search section
# after each successful search, the ticker can be added to a list and then for subsequent searches it can just check if its in the list 
# to avoid going through the whole process again?
#print(ticker.dividends)
## ok can have a dropdown that has the different periods, 1 day, 1 week, 1 month et 
## can havw
# AAPL: Period '1h' is invalid, must be one of ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
# Empty DataFrame
# Columns: [Open, High, Low, Close, Adj Close, Volume]
# Index: [] 


#print(div_df)s
#print(div_df["Dividends"])

#print(f"current dividend rate: {ticker.info["dividendYield"]}") 

app.layout = html.Div([
    html.H1("fincance bros portfolio 101 get rich quick", style={"text-align": "centre"}),
    dcc.Dropdown(id="period",
                    options=[
                        {"label": "1 Day", "value": "1d"},
                        {"label": "5 Days", "value": "5d"},
                        {"label": "1 Month", "value": "1mo"},
                        {"label": "3 Months", "value": "3mo"},
                        {"label": "6 Months", "value": "6mo"},
                        {"label": "1 Year", "value": "1y"},
                        {"label": "Year to Date", "value": "ytd"},
                        {"label": "Max", "value": "max"},
                    ],
                    value="1d",
                    multi=False,
                    style={"width": "40%"}

    ),
    dcc.Input(id="ticker_input", type="text", placeholder="AAPL", style={'marginRight':'10px'}),
    html.Br(),
    html.Div(id="current_price", children=[]),
    dcc.Graph(id="stock_graph", figure={})
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

    #print(ticker.info["currentPrice"])
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

## can replace the ebita with other info or just dont specify and get all the available information
