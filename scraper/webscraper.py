from scraper.urlloader import URLLoader
from scraper.parser import Parser

class WebScraper:
    def __init__(self, url_file):
        self.url_loader = URLLoader(url_file)
        self.parser = Parser()

    def scrape(self):
        urls = self.url_loader.load()
        for url in urls:
            title = self.parser.fetch_title(url)
            links = self.parser.fetch_links(url)

            print(f"URL: {url}\nTitel: {title}\n")

            if links:
                with open("save_data/links.txt", "a") as links_file:
                    for link in links:
                        links_file.write(f"{link}\n")
