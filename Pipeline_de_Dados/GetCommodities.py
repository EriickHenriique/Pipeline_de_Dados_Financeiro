import yfinance as yf
from datetime import datetime
import pandas as pd

def get_commodities_df():
    symbols = ['GC=F','CL=F','SI=F']
    dfs = []
    for syn in symbols:
        ultimo_df = yf.Ticker(syn).history(period='1d', interval='1m')[['Close']].tail(1)
        ultimo_df = ultimo_df.rename(columns={'Close':'preco'})
        ultimo_df['ativo'] = syn
        ultimo_df['moeda'] = 'USD'
        ultimo_df['hora'] = datetime.now().strftime('%H:%M:%S')
        ultimo_df = ultimo_df[['hora','ativo','preco','moeda']]
        dfs.append(ultimo_df)
    return pd.concat(dfs, ignore_index=True)






