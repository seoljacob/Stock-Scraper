from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os

FILE_PATH = '/Users/jacobseol/Projects/Stock-Scraper/stock_data2.csv'

class StoreData:
    _data = []
    _first_write = True

    @staticmethod
    def get_stock_data(ticker: str):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}')

        # Wait for the table to be loaded
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(class_='W(100%) M(0)')
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        
        for row in rows:
            cells = row.find_all('td')
            if cells:
                date = cells[0].text

                # Check if a closing value exists
                if len(cells) > 4:
                    close = cells[4].text
                    StoreData._data.append({"ticker": ticker, "date": date, "close": close})
                else:
                    print(f'{date}: No closing value available')
        print(f'Successfully retrieved stock data for: {ticker}')
        driver.close()

    @staticmethod
    def get_all(tickers: list, file_name: str):
        for ticker in tickers:
            try:
                StoreData.get_stock_data(ticker)
                StoreData.write_to_csv(file_name)
            except Exception as e:
                print(f'Error has occured: {e}')


    @staticmethod
    def write_to_csv(file_name: str):
        df = pd.DataFrame(StoreData._data)
        if not os.path.isfile(FILE_PATH):
            df.to_csv(file_name, index=False)
            print("File does not exist, writing to new file")
        else:
            df.to_csv(file_name, mode='a', header=False, index=False)
            print("File exists, appending to existing file")
        print(f'Successfully wrote to: {file_name}')
        StoreData._data.clear()


if __name__ == "__main__":
    StoreData.get_stock_data("GOOG")
    print(StoreData._data)