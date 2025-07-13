import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send GET request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote text on the page
quotes = soup.find_all("span", class_="text")

for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote.text}")


