import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('swaprate.csv')
table_name = "swaprate"
DB_name = "market_data"

#コメント テーブルは事前に作らなくてOK！"swaprate"ここで作られる。


db_settings = {
    "host": 'localhost',
    "database": DB_name,
    "user": 'root',
    "password": '●●',
    "port":3306
}

engine = create_engine('mysql://{user}:{password}@{host}:{port}/{database}'.format(**db_settings))

df.to_sql(table_name, engine, DB_name, index=False)

#df.to_sql(table_name, engine, 'trade', index=False)
#コメント'trade'→DB名

