import requests
from bs4 import BeautifulSoup

class URLLoader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        with open(self.file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]

class Parser:
    def fetchTitle(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup.title.string if soup.title else "Geen titel gevonden"
            else:
                return f"Fout bij ophalen van {url}: {response.status_code}"
        except requests.RequestException as e:
            return f"Error at {url}: {e}"

    def fetchLink(selfself, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = []
                for a in soup.find_all('a', href=True):
                    links.append(a['href'])

                links_file = open("save_data/links.txt", "a")
                for x in links:
                    if x.startswith("https://") or x.startswith("http://"):
                        links_file.write(f"{x}\n")
                    else:
                        links_file.write(f"{url}{x}\n")

            else:
                print('Error getting URL')
        except requests.RequestException as e:
            return f"Error at {url}: {e}"

class WebScraper:
    def __init__(self, url_file):
        self.url_loader = URLLoader(url_file)
        self.title_fetcher = Parser()

    def scrape(self):
        urls = self.url_loader.load()
        for url in urls:
            title = self.title_fetcher.fetchTitle(url)
            links = self.title_fetcher.fetchLink(url)
            print(f"URL: {url}\nTitel: {title}\n")

if __name__ == "__main__":
    scraper = WebScraper("save_data/urls.txt")
    scraper.scrape()
