import requests
from bs4 import BeautifulSoup
import re

class Parser:
    def fetch_title(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string if soup.title else "No title found"
                return str(title)
            else:
                return f"Fout bij ophalen van {url}: {response.status_code}"
        except requests.RequestException as e:
            return f"Error at {url}: {e}"

    def fetch_links(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return [
                    a['href'] if a['href'].startswith(('http://', 'https://')) else f"{url}{a['href']}"
                    for a in soup.find_all('a', href=True)
                ]
            else:
                return []
        except requests.RequestException:
            return []

    def fetch_metadescription(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            meta_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
            if meta_tag:
                meta_data = meta_tag.get("content", "")
                if meta_data:
                    return meta_data
                else:
                    return
            else:
                return

    def fetch_metatitle(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            meta_title = soup.find("meta", attrs={"name": "title"}) or soup.find("meta", attrs={"property": "og:title"})
            if meta_title:
                meta_data = meta_title.get("content", "")
                if meta_data:
                    return meta_data
                else:
                    return
            else:
                return