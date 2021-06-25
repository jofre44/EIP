from datetime import date
import pandas as pd
import yfinance as yf
import datetime as dt
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

app = dash.Dash(__name__)

STOCKS_OPTIONS = {
    'Google': 'GOOG',
    'Apple': 'AAPL',
    'Tesla': 'TSLA',
    'Microsoft': 'MSFT',
    'Facebook':  'FB',
    'Netflix': 'NFLX',
    'General Motors': 'GM',
    'Coca Cola': 'KO',
    'Walmart': 'WMT',
    'Visa': 'V',
    'Disney': 'D'
}

def get_options(dict_stocks):
    dict_list = []
    for i in dict_stocks.keys():
        dict_list.append({'label': i, 'value': dict_stocks[i]})

    return dict_list


df_stocks = None

for stock in STOCKS_OPTIONS.values():
    df = yf.download(stock, '2015-1-1', str(dt.date.today()))
    df.rename(columns={'Adj Close': stock}, inplace=True)
    if df_stocks is None:
        df_stocks = df[[stock]]
    else:
        df_stocks = pd.concat([df_stocks, df[stock]], axis=1)

app.layout = html.Div(children=[html.H1("Stocks Comparison"),
                                html.H3("Alumno: Jose Sepulveda"),
                                html.H4("Select Stocks to Plot"),
                                dcc.Dropdown(id='stockselector',
                                            options=get_options(STOCKS_OPTIONS),
                                            multi=True,
                                            value=['GOOG','MSFT']),
                                html.H4("Select Date Range"),
                                dcc.DatePickerRange(id='my-date-picker-range',
                                                    min_date_allowed=date(2015, 1, 1),
                                                    max_date_allowed=date.today(),
                                                    initial_visible_month=date(2015, 1, 1),
                                                    start_date=date(2015, 1, 1),
                                                    end_date=date.today()),
                                dcc.Graph(id='stock_normalize_evolution', config={'displayModeBar': False}),
                                dcc.Graph(id='stock_monthly_return', config={'displayModeBar': False}),
                                dcc.Graph(id='stock_correlation', config={'displayModeBar': False})])


@app.callback(Output('stock_normalize_evolution', 'figure'),
              [Input('stockselector', 'value'),
              Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date')])
def update_timeseries(selected_dropdown_value, start_date, end_date):

    df = df_stocks[selected_dropdown_value].copy()
    df = df.loc[start_date:end_date]
    for stock in selected_dropdown_value:
        first_value = df[stock][0]
        df[stock] = df[stock] / first_value

    figure_line = px.line(df, title = "Normalize Evolution")
    return figure_line

@app.callback(Output('stock_monthly_return', 'figure'),
              [Input('stockselector', 'value'),
              Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date')])
def update_daily_return(selected_dropdown_value, start_date, end_date):
    
    df = df_stocks[selected_dropdown_value].copy()
    df = df.loc[start_date:end_date]
    df_month = df.asfreq('M').ffill()
    df_return = (df_month/df_month.shift(1))-1

    figure_return = px.bar(df_return, barmode='group', title='Monthly Return')
    return figure_return

@app.callback(Output('stock_correlation', 'figure'),
              [Input('stockselector', 'value'),
              Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date')])
def update_daily_return(selected_dropdown_value, start_date, end_date):

    df = df_stocks[selected_dropdown_value].copy()
    df = df.loc[start_date:end_date]
    df_corr = df.corr()

    figure_corr = go.Figure(go.Heatmap(z=df_corr.values,
                            x=df_corr.index.values,
                            y=df_corr.columns,
                            colorscale=['red', 'white', 'green']))

    figure_corr.update_layout({'title':'Stocks Correlation'})
    return figure_corr


if __name__ == '__main__':
    app.run_server(debug=True)