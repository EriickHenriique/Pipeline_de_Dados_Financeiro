import time
import pandas as pd
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

SLEEP_SECONDS = 60

if __name__ == "__main__":
    while True:
        # Coleta
        df_btc = get_bitcoin_df()
        df_comm = get_commodities_df()

        # Junta tudo
        df = pd.concat([df_btc, df_comm], ignore_index=True)

        # Imprime
        print(df)

        # Espera próximo ciclo
        time.sleep(SLEEP_SECONDS)