import yfinance as yf
from datetime import datetime
import pandas as pd

def get_commodities_df():
    symbols = ['GC=F','CL=F','SI=F']
    dfs = []
    for syn in symbols:
        ultimo_df = yf.Ticker(syn).history(period='1d', interval='1m')[['Close']].tail(1)
        ultimo_df = ultimo_df.rename(columns={'Close':'Preço'})
        ultimo_df['Ativo'] = syn
        ultimo_df['Moeda'] = 'USD'
        ultimo_df['Horário'] = datetime.now()
        ultimo_df = ultimo_df[['Horário','Ativo','Preço','Moeda']]
        dfs.append(ultimo_df)
    return pd.concat(dfs, ignore_index=True)






