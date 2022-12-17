from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')

# Wait for the table to be loaded
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
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

