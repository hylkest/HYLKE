from scraper.webscraper import WebScraper

if __name__ == "__main__":
    scraper = WebScraper("save_data/urls.txt")
    scraper.scrape()
