# Stock-Scraper

This is a preliminary step to building an autonomous stock trading bot, where I gather historical stock data.

The process:
1. Set up a Selenium webdriver that establishes a connection to Yahoo Finance.
2. Wait for Yahoo Finance to load the website fully. This step is necessary as stock ticker data is being generated dynamically and may not be present in the HTML when the page is initially loaded.
3. Use BeautifulSoup to parse the website's HTML.
4. Extract data.

