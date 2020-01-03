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
#ここでmysql上の”USSWAP10”というカラムを選択する。
USSWAP10.to_csv('result/USSWAP10.csv')

diff=USSWAP10.diff()

diff.to_excel('result/swaprate_diff.xlsx')

print(diff.describe())
diff.describe().to_excel('result/describee.xlsx')

diff.plot()
plt.savefig('result/b'+'.png')
plt.savefig('result/b'+".pdf", format='pdf', bbox_inches='tight')
plt.show()
