import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(filename='logs/scraper.log', level=logging.INFO)

def scrape_jumia(url):
    logging.info(f"Starting scrape for URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f"Successfully fetched the page: {url}")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all product containers
        product_containers = soup.find_all('article', class_='prd _fb col c-prd')

        data = []
        for container in product_containers:
            try:
                # Extract product title
                title_element = container.find('h3', class_='name')
                title = title_element.get_text(strip=True) if title_element else "N/A"
                
                # Extract product price
                price_element = container.find('div', class_='prc')
                price = price_element.get_text(strip=True) if price_element else "N/A"
                
                # Extract product link
                link_element = container.find('a', class_='link')
                link = link_element['href'] if link_element else None
                full_link = f"https://www.jumia.co.ke{link}" if link else "N/A"
                
                # Append extracted data to the list
                data.append({
                    'Title': title,
                    'Price': price,
                    'Link': full_link
                })
            except Exception as e:
                logging.error(f"Error extracting product details: {e}")

        logging.info(f"Scraped {len(data)} products")
        return data
    else:
        logging.error(f"Failed to fetch the page: {url} with status code {response.status_code}")
        return []

