import yfinance as yf
import pandas as pd

ticker_list =[]
buy_price_list=[]
buy_count_list=[]
df_list = []
datacsv = pd.DataFrame()
data = pd.DataFrame()
def get_symbols():
    global ticker_list , buy_price_list, buy_count_list
    global datacsv
    colnames = ['SYMBOL', 'BUY_PRICE', 'COUNT']
    datacsv = pd.read_csv('stocks.csv', names=colnames, header=0)
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
    # print(data)
    global df_list
    col_start = 0
    for i in range(len(ticker_list)):
        # print(ticker_list[i],",",buy_price_list[i],",",buy_count_list[i])
        # 0:4 =0 , 5:9,
        col_end = col_start + 4 
        df = pd.DataFrame()
        df = data.iloc[:,col_start:col_end]
        first_symbol_data = list( df.columns.values)
        symbol = first_symbol_data[0][0]

        # print(symbol,",",lookup_cost(symbol),",",lookup_count(symbol))
        # add new colummns in DF
        # print(df.columns.values[3])
        buy_cost= lookup_cost(symbol)
        buy_count =lookup_count(symbol)
        total_cost = buy_cost * buy_count
        tot_curr_cost = df[df.columns.values[3]] * buy_count
        df['GAIN_LOSS']= df[df.columns.values[3]] - buy_cost
        df['TOT_GAIN_LOSS']=  tot_curr_cost - (buy_cost*buy_count)
        
        df_list.append(df)
        print(df)
        col_start = col_start+5

    # print(first_symbol_data.iloc[0:0,0:1])

def lookup_cost(symbol):
    match = (datacsv['SYMBOL'] == symbol) 
    cost = datacsv['BUY_PRICE'][match]
    return cost.values[0]

def lookup_count(symbol):
    match = (datacsv['SYMBOL'] == symbol) 
    count = datacsv['COUNT'][match]
    return count.values[0]

get_symbols()