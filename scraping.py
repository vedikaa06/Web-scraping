from bs4 import BeautifulSoup
import requests
from headers import load_headers
import time
import json

def fetch_page_content(url):
    """
    Fetch HTML content of the page using requests and custom headers.

    Parameters:
        url (str): The URL to fetch.

    Returns:
        str: The raw HTML content of the page.
    """
    print(f"Attempting to fetch data from: {url}")
    time.sleep(1)  # Be polite to the server
    response = requests.get(url, headers=load_headers(), timeout=10)
    response.raise_for_status()
    print(f"Successful! Status Code: {response.status_code}")
    return response.content

def parse_quotes(html_content):
    """
    Parse HTML content to extract quotes, authors, and tags.

    Parameters:
        html_content (str): HTML source of the page.

    Returns:
        list[dict]: A list of dictionaries with quote data.
    """
    soup = BeautifulSoup(html_content, 'lxml')
    quote_elements = soup.find_all('div', class_='quote')

    quotes = []

    for quote in quote_elements:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.find_all('a', class_='tag')]

        quotes.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    return quotes

def save_to_json(data, filename):
    """
    Save the data to a JSON file.

    Parameters:
        data (list): The data to write.
        filename (str): The name of the output file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

def main():
    """
    Main function to control scraping logic.
    """
    url = "https://quotes.toscrape.com/"
    try:
        html = fetch_page_content(url)
        quotes = parse_quotes(html)
        print(quotes)  # Optional: verify output
        save_to_json(quotes, "quotes_data.json")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
