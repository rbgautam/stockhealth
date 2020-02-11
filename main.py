import yfinance as yf
import pandas
colnames = ['SYMBOL', 'BUY_PRICE', 'COUNT']
datacsv = pandas.read_csv('stocks.csv', names=colnames, header=1)


# Stock names = 
ticker_list = datacsv.SYMBOL.tolist()

print(ticker_list)

data = yf.download(  tickers = ticker_list,    
        period = "3mo",
        interval = "5d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

print(data)