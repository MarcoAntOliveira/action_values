import yfinance as yf
import pandas as pd

# Defina o ticker da ação que você deseja obter os valores
ticker = "ABNB"  # Exemplo: Apple Inc.


# Use a função 'download' para obter os dados históricos
data = yf.download(ticker, start="2023-01-01", end="2023-11-20")
print(data)
action = pd.DataFrame(data)
action.to_excel('dados_de_acao.xlsx', index=False)
print(action)


