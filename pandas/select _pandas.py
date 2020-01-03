import MySQLdb
import MySQLdb.cursors   # 追加！
import pandas as pd


connection=MySQLdb.connect(
    host="localhost",user="root",
    passwd="●●",db="market_data",
    cursorclass = MySQLdb.cursors.SSCursor)# 追加！

df = pd.read_sql("SELECT * FROM zoo", connection)
print(df)
print(df.damages)

a=df.damages
a.to_csv('test.csv')
