from scraper.urlloader import URLLoader
from scraper.parser import Parser
from scraper.database import Database
import time

class WebScraper:
    def __init__(self, url_file):
        self.url_loader = URLLoader(url_file)
        self.parser = Parser()
        self.database = Database()

    def scrape(self):
        urls = self.url_loader.load()
        for url in urls:
            titles = self.parser.fetch_title(url)
            links = self.parser.fetch_links(url)
            metadata = self.parser.fetch_metadata(url)
            time.sleep(1)

            for link in links:
                self.database.insert_link(url, link)

            self.database.insert_pagetitle(url, titles)
            self.database.insert_metadata(url, metadata)
