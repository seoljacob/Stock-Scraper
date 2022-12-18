from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class StoreData:
    _data = []
    _first_write = True

    @staticmethod
    def get_stock_data(ticker: str):
        # Set up the webdriver
        options = webdriver.ChromeOptions()

        # Set up a headless browser to increase performance (a headless browser does not have a GUI but can still run commands)
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options)

        # Navigate to the website
        driver.get(f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}')

        # Wait for the table to be loaded
        html = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(html, 'html.parser')

        # Find the table containing the stock information
        table = soup.find(class_='W(100%) M(0)')

        # Find the data you want to extract
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')

        # Extract the data from the HTML elements
        for row in rows:
            cells = row.find_all('td')
            if cells:  # Make sure the row contains data
                date = cells[0].text

                # Check if a closing value exists
                if len(cells) > 4:
                    close = cells[4].text
                    # print(f'{date}: {close}')
                    StoreData._data.append({"ticker": ticker, "date": date, "close": close})
                else:
                    print(f'{date}: No closing value available')
        print(f'Successfully retrieved stock data for: {ticker}')
        # Close the web browser
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
        if StoreData._first_write:
            df.to_csv(file_name, index=False)
            StoreData._first_write = False
        else:
            df.to_csv(file_name, mode='a', header=False, index=False)
        print(f'Successfully wrote to: {file_name}')
        StoreData._data.clear()


if __name__ == "__main__":
    StoreData.get_stock_data("GOOG")
    print(StoreData._data)