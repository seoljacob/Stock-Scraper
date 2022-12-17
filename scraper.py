from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def get_stock_tickers():
    # Use requests to retrieve the HTML of the Wikipedia page for the S&P 500 index
    response = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    # Use BeautifulSoup to parse the HTML and extract the tickers
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = [row.find_all('td')[0].text.strip() for row in table.find_all('tr')[1:]]

    print(tickers)


def scrape_stock_data(ticker: str):
    # Set up the webdriver
    driver = webdriver.Chrome()

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
                print(f'{date}: {close}')
            else:
                print(f'{date}: No closing value available')

    # Close the web browser
    driver.close()

if __name__ == "__main__":
    # scrape_stock_data("GOOG")
    get_stock_tickers()