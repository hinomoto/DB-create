import MySQLdb
import MySQLdb.cursors   # 追加！
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



connection=MySQLdb.connect(
    host="localhost",user="root",
    passwd="●●",db="market_data",
    cursorclass = MySQLdb.cursors.SSCursor)# 追加！

df = pd.read_sql("SELECT * FROM swaprate", connection)

USSWAP10=df.USSWAP10
USSWAP10.to_csv('USSWAP10.csv')
