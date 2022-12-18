from tickers import Tickers
from scraper import StoreData
import datetime

if __name__ == "__main__":
    t = Tickers()
    t.get_stock_tickers()
    print(f'Start time: {datetime.datetime.now()}')
    StoreData.get_all(t.ticker_list, 'stock_data2.csv')
    print(f'End time: {datetime.datetime.now()}')
