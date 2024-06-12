import os
from scraper.scraper import scrape_jumia
from scraper.data_processing import process_data
from config import BASE_URL

def main():
    # Scrape raw data from Jumia
    raw_data = scrape_jumia(BASE_URL)
    
    if raw_data:
        # Process the scraped data
        processed_data = process_data(raw_data)
        
        # Ensure the processed data directory exists
        output_directory = 'data/processed'
        os.makedirs(output_directory, exist_ok=True)
        
        # Save the processed data to a CSV file
        processed_data_path = os.path.join(output_directory, 'jumia_products.csv')
        processed_data.to_csv(processed_data_path, index=False)
        print(f"Data saved to '{processed_data_path}'")
    else:
        print("No data scraped. Please check the logs for more details.")

if __name__ == "__main__":
    main()
