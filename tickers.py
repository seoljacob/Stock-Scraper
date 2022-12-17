from bs4 import BeautifulSoup
import requests

class Tickers:
    def __init__(self):
        self._ticker_list = None

    @property
    def ticker_list(self):
        if self._ticker_list:
            return self._ticker_list
        else:
            print("No ticker data.")

    @ticker_list.setter
    def ticker_list(self, value):
        self._ticker_list = value
    
    
    def get_stock_tickers(self):
        # Use requests to retrieve the HTML of the Wikipedia page for the S&P 500 index
        response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

        # Use BeautifulSoup to parse the HTML and extract the tickers
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'wikitable sortable'})
        self.ticker_list = ([row.find_all('td')[0].text.strip() for row in table.find_all('tr')[1:]])

if __name__ == "__main__":
    test = Tickers()
    test.get_stock_tickers()
    for ticker in test.ticker_list:
        print(ticker)
    print(len(test.ticker_list))
    