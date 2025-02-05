from scraper.urlloader import URLLoader
from scraper.parser import Parser
from scraper.database import Database
import time
import random

class WebScraper:
    def __init__(self):
        self.url_loader = URLLoader()
        self.parser = Parser()
        self.database = Database()

    def scrape(self):
        urls = self.url_loader.load()
        for url in urls:
            print(f"Start scraping URL: {url}")
            titles = self.parser.fetch_title(url)
            links = self.parser.fetch_links(url)
            metadesc = self.parser.fetch_metadescription(url)
            metatitle = self.parser.fetch_metatitle(url)

            for link in links:
                self.database.insert_link(url, link)

            self.database.insert_pagetitle(url, titles)
            self.database.insert_metadata(url, metatitle, metadesc)
            print(f"Done scraping URL: {url}")
            delay = random.uniform(1, 5)
            time.sleep(delay)
