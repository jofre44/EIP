import pandas as pd
import yfinance as yf
import plotly.express as px
import streamlit as st

NUM_OPTIONS = {
    'Payout Ratio': 'payoutRatio',
    'Dividend Rate': 'dividendRate',
    'Beta': 'beta',
    'Market Cap': 'marketCap',
    'Book Value': 'bookValue',
    'Price To Book': 'priceToBook',
    'Market Price': 'regularMarketPrice',
    'Price To Earnigs': 'trailingPE',
    'Employees': 'fullTimeEmployees'
}

STR_OPTIONS = {
    'Sector': 'sector',
    'City': 'city',
    'State': 'state',
    'Country': 'country',
    'Industry': 'industry',
}
LIST_OPTIONS ={**STR_OPTIONS, **NUM_OPTIONS}

st.sidebar.title('Stock from SP500 Analisys')
st.sidebar.write('Alumno: Jose Sepulveda')

option_1 = st.sidebar.selectbox('Seleccione primer nivel de agregación del mapa de acciones:', tuple(STR_OPTIONS.keys()), index=0)
option_2 = st.sidebar.selectbox('Seleccione segundo nivel de agregación del mapa de acciones:', tuple(STR_OPTIONS.keys()), index=4)
option_3 = st.sidebar.selectbox('Seleccione variable para tamaño de las cajas de las de acciones:', tuple(NUM_OPTIONS.keys()), index=3)


option_4 = st.sidebar.selectbox('Seleccione nivel x del gráfico de dispersión:', tuple(NUM_OPTIONS.keys()), index=3)
option_5 = st.sidebar.selectbox('Seleccione nivel y del gráfico de dispersión:', tuple(NUM_OPTIONS.keys()), index=8)
option_6 = st.sidebar.selectbox('Seleccione color del grafico de disperioón:', tuple(STR_OPTIONS.keys()), index=0)

p = st.empty()
try: 
    combined_data = pd.read_csv('stock_fundametals.csv')
    combined_data.columns = ["Stock", "Drop","Attribute", "Recent"]    
    combined_data = combined_data[["Stock", "Attribute", "Recent"]]
    combined_data = combined_data[combined_data['Attribute'].isin(LIST_OPTIONS.values())]
except:
    table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    df = table[0]
    stocks_tck = list(df.Symbol)

    tickers_data= {}
    i = 1
    for tick in stocks_tck:
        ticker_object = yf.Ticker(tick)

        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
        temp.reset_index(inplace=True)
        temp.columns = ["Attribute", "Recent"]
        tickers_data[tick] = temp
        percentage = round((i/len(stocks_tck))*100,2)
        p.write(f"Downloading data: {percentage} %")
        i +=1
    combined_data = pd.concat(tickers_data)
    combined_data.to_csv('stock_fundametals.csv')
    combined_data.reset_index(inplace=True)
    combined_data.columns = ["Stock", "Drop","Attribute", "Recent"]    
    combined_data = combined_data[["Stock", "Attribute", "Recent"]]
    combined_data = combined_data[combined_data['Attribute'].isin(LIST_OPTIONS.values())]

p.write("") 
df_wide = combined_data.pivot(index='Stock', columns='Attribute', values='Recent')
df_wide.fillna(0, inplace=True)
df_wide.reset_index(inplace=True)
df_wide[list(NUM_OPTIONS.values())] = df_wide[list(NUM_OPTIONS.values())].apply(pd.to_numeric)

if not st.checkbox("Ocultar mapa de acciones"):
    st.title('Mapa de Acciones')
    fig = px.treemap(df_wide, path=[LIST_OPTIONS[option_1], LIST_OPTIONS[option_2], 'Stock'], values=LIST_OPTIONS[option_3],
                    color=LIST_OPTIONS[option_2], color_continuous_scale='RdBu')
    st.plotly_chart(fig)

st.title('Dispersión de Acciones')
fig = px.scatter(df_wide, x =LIST_OPTIONS[option_4], y=LIST_OPTIONS[option_5], color=LIST_OPTIONS[option_6], hover_name='Stock',
                labels={
                     LIST_OPTIONS[option_4]: option_4,
                     LIST_OPTIONS[option_5]: option_5,
                     LIST_OPTIONS[option_6]: option_6})
st.plotly_chart(fig)