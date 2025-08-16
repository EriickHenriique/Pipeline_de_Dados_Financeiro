import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():

    # URL da Coinbase para obter o preço atualizado do Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    #Requisição na API e Definição da variável
    response = requests.get(url)
    data = response.json()

    #Separando as informações do JSON
    price = float(data['data']['amount'])
    asset = data['data']['base']
    currency = data['data']['currency']
    time = datetime.now().strftime('%H:%M:%S')

    # Criação do DataFrame
    df = pd.DataFrame([{
        'hora': time,
        'ativo': asset,
        'preco': price,
        'moeda': currency
    }])

    return df


