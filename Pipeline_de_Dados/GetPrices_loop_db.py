import time
import pandas as pd
from sqlalchemy import create_engine
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df
from dotenv import load_dotenv
import os

SLEEP_SECONDS = 60

load_dotenv()

# Configuração do banco (substituir com seus dados reais)
DB_USER = os.getenv("user")
DB_PASSWORD = os.getenv("password")
DB_HOST = os.getenv("host")
DB_PORT = os.getenv("port")
DB_NAME = os.getenv("dbname")

# Criar conexão SQLAlchemy
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

if __name__ == "__main__":
    while True:
        # Coleta
        df_btc = get_bitcoin_df()
        df_comm = get_commodities_df()

        # Junta tudo
        df = pd.concat([df_btc, df_comm], ignore_index=True)

        # Salva no banco (append)
        df.to_sql("cotacoes", engine, if_exists="append", index=False)

        print("✅ Cotações inseridas no banco com sucesso!")

        # Espera próximo ciclo
        time.sleep(SLEEP_SECONDS)