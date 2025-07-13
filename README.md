# Python Web Scraper — Quotes Extractor

## What it does

This Python program scrapes quotes from the website [quotes.toscrape.com](https://quotes.toscrape.com/). It fetches the page content, parses the HTML, and extracts all quotes displayed on the homepage. The quotes are then printed one by one in the terminal.

## How to run it

1. Make sure you have Python 3 installed.  

2. Activate your virtual environment (if you use one):  
   ```bash
   source myenv/bin/activate
   ```

3. Install required packages:  
   ```bash
   pip install requests beautifulsoup4
   ```

4. Run the scraper:  
   ```bash
   python scraper.py
   ```

## What I learned

- How to send HTTP requests and handle responses using the `requests` library.  
- How to parse HTML content using `BeautifulSoup` to extract specific elements.  
- Basic concepts of web scraping and data extraction.  
- How to work with Python virtual environments to manage dependencies.
