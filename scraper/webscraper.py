from scraper.urlloader import URLLoader
from scraper.parser import Parser
from scraper.database import Database

class WebScraper:
    def __init__(self, url_file):
        self.url_loader = URLLoader(url_file)
        self.parser = Parser()
        self.database = Database()

    def scrape(self):
        urls = self.url_loader.load()
        for url in urls:
            title = self.parser.fetch_title(url)
            links = self.parser.fetch_links(url)

            print(f"URL: {url}\nTitel: {title}\n")

            for link in links:
                self.database.insert_link(link)
