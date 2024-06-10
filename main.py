from scraper.scraper import scrape_jumia
from scraper.data_processing import process_data
from config import BASE_URL

def main():
    # Step 1: Scrape data
    raw_data = scrape_jumia(BASE_URL)

    # Step 2: Process data
    processed_data = process_data(raw_data)

    # Save the processed data to a file
    processed_data.to_csv('data/processed/jumia_products.csv', index=False)

if __name__ == "__main__":
    main()
