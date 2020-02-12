import yfinance as yf
import pandas as pd

ticker_list =[]
buy_price_list=[]
buy_count_list=[]

data = pd.DataFrame()
def get_symbols():
    global ticker_list , buy_price_list, buy_count_list

    colnames = ['SYMBOL', 'BUY_PRICE', 'COUNT']
    datacsv = pd.read_csv('stocks.csv', names=colnames, header=1)
    # Stock names 
    ticker_list = datacsv.SYMBOL.tolist()
    buy_price_list= datacsv.BUY_PRICE.tolist()
    buy_count_list = datacsv.COUNT.tolist()
    get_historical_data()


def get_historical_data():
    global data 
    # print(ticker_list)
    data = yf.download(  tickers = ticker_list,    
            period = "3mo",
            interval = "5d",
            group_by = 'ticker',
            auto_adjust = True,
            prepost = True,
            threads = True,
            proxy = None
        )
    slice_data()

def slice_data():
    print(data)
    df_list = []
    col_start = 0
    for i in range(len(ticker_list)):
        # print(ticker_list[i],",",buy_price_list[i],",",buy_count_list[i])
        # 0:4 =0 , 5:9,
        col_end = col_start + 4 
        df = pd.DataFrame()
        df = data.iloc[:,col_start:col_end]
        df_list.append(df)
        # print(df)
        col_start = col_start+5
    # print(len(ticker_list))






get_symbols()