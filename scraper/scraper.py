import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(filename='logs/scraper.log', level=logging.INFO)

def scrape_jumia(url):
    logging.info(f"Starting scrape for URL: https://www.jumia.co.ke/")
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f"Successfully fetched the page: https://www.jumia.co.ke/")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Your scraping logic here
        product_containers = soup.find_all('article', class_='prd _fb col c-prd')
        
        data = []
        for container in product_containers:
            title = container.find('h3', class_='name').get_text(strip=True)
            price = container.find('div', class_='prc').get_text(strip=True)
            link = container.find('a', class_='link')['href']
            full_link = f"https://www.jumia.co.ke"
            data.append({
                'Title': title,
                'Price': price,
                'Link': full_link
            })
        
        logging.info(f"Scraped {len(data)} products")
        return data
    else:
        logging.error(f"Failed to fetch the page: {url} with status code {response.status_code}")
        return []

