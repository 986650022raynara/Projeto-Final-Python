import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Título do app
st.title('Stock History App')

# Criando o sidebar
st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

# Baixando dados do yahoo finaças
data = yf.download(ticker_symbol, start = '2020-01-01', end = '2023-06-26')

# Calcular a EMA usando pandas
window = 20  # Janela da EMA
data['EMA'] = data['Close'].ewm(span=window, adjust=False).mean()

# Exibir os dados
st.subheader('Histórico')
st.dataframe(data)

# Exibir o gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name = 'Fechamento'))
fig.add_trace(go.Scatter(x=data.index, y=data['EMA'], name='EMA'))

fig.update_layout(title = f"{ticker_symbol}", xaxis_title = "Data", yaxis_title = "Preço")
st.plotly_chart(fig)