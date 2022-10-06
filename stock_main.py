# from stock_module import crap_data
import stock_module as m
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt

all = []
symbol,dates = m.get_data()

for date in dates:
    sleep(5)
    # try:
    crap_data = m.crap_data(date,symbol)
    all.append(crap_data[0])
    df_columns = crap_data[1]
        # print("right")
    # except:
    #     print("wrong")

all_df = pd.DataFrame(all,columns=df_columns)
# print(all_df)

# day = all_df["日期"].astype(str)
# close = all_df["收盤價"].astype(float)

# plt.figure(figsize=(20,10),dpi=100)

# plt.plot(day,close,'s-',color = 'r',label = "Close Price")
# plt.title("TSMC Line Chart")
# plt.xticks(fontsize=10,rotation=45)
# plt.yticks(fontsize=10)
# plt.legend(loc="best",fontsize=20)

# plt.show()