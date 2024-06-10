import unittest
from scraper.scraper import scrape_jumia
from config import BASE_URL

class TestScraper(unittest.TestCase):

    def test_scrape_jumia(self):
        data = scrape_jumia(BASE_URL)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('Title', data[0])
        self.assertIn('Price', data[0])
        self.assertIn('Link', data[0])

if __name__ == '__main__':
    unittest.main()
