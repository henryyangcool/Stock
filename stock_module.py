import requests
import pandas as pd
from io import StringIO
import datetime

# date = "20221003"
# stock_symbol = "2885"

def setting():
    res = []
    # try:
    #     with open("stockdata.txt") as f:
    #         slist = f.readlines()
    #         print("讀入:",slist)
    #         a,b,c = slist[0].split(",")
    #         res = [a,b,c]
    # except:
    #     print("stock.txt讀取錯誤")
    res = ["2330","20210930","20221006"]
    return res

def crap_data(date,symbol):
    r = requests.get("https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=" + date + "&type=ALLBUT0999")

    # print(r.text)
    # r_text = r.text.split('\n')
    r_text = [i for i in r.text.split("\n") if len(i.split('",')) == 17 and i[0] != "="]
    df = pd.read_csv(StringIO("\n".join(r_text)),header=0)

    df = df.drop(columns=["Unnamed: 16"])
    filter_df = df[df["證券代號"] == symbol]
    filter_df.insert(0,"日期",date)
    df_columns = filter_df.columns

    return list(filter_df.iloc[0]), df_columns

def get_data():
    data = setting()
    dates = []
    start_date = datetime.datetime.strptime(data[1],"%Y%m%d")
    end_date = datetime.datetime.strptime(data[2],"%Y%m%d")

    for daynum in range((end_date - start_date).days + 1):
        date = (start_date + datetime.timedelta(days=daynum))
        if date.weekday() < 6:
            dates.append(date.strftime("%Y%m%d"))
    
    return data[0],dates