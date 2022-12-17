# Stock-Scraper

This is a preliminary step to building an autonomous stock trading bot, where I gather historical stock data.

## The Process
1. Set up a Selenium webdriver that establishes a connection to Yahoo Finance.
2. Wait for Yahoo Finance to load the website fully. This step is necessary as stock ticker data is being generated dynamically and may not be present in the HTML when the page is initially loaded.
3. Use BeautifulSoup to parse the website's HTML.
4. Extract data.

## The Challenge
The above process is to retrieve stock data for a single ticker. The autonomous stock trading bot will need access to data for multiple stocks (ie. the stocks for the entire S&P 500 stock index)

To retrieve active S&P 500 stock tickers, make a request to Wikipedia and parse the ticker data.
