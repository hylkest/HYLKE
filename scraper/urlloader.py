from scraper.database import Database

class URLLoader:
    def __init__(self):
        self.database = Database()

    def load(self):
        return self.database.get_urls()
