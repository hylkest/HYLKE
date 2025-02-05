import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=os.getenv("SQL_HOST"),
            user=os.getenv("SQL_USERNAME"),
            password=os.getenv("SQL_PASSWORD"),
            database=os.getenv("SQL_DB"),
            port=3306
        )
        self.mycursor = self.mydb.cursor()

    def get_urls(self):
        sql_query = "SELECT url FROM links"
        self.mycursor.execute(sql_query)
        return [row[0] for row in self.mycursor.fetchall()]

    def insert_link(self, base_url, url):
        sql_query = """
        INSERT INTO links (base_url, url)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE base_url = VALUES(base_url)
        """
        self.mycursor.execute(sql_query, (base_url, url,))
        self.mydb.commit()

    def insert_pagetitle(self, url, pagetitle):
        sql_query = """
        INSERT INTO pagetitle (pagetitle, url)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE pagetitle = VALUES(pagetitle)
        """
        self.mycursor.execute(sql_query, (pagetitle, url,))
        self.mydb.commit()

    def insert_metadata(self, url, metatitle, metadata):
        sql_query = """
        INSERT INTO meta (url, meta_title, meta_description)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE meta_title = %s, meta_description = %s
        """
        self.mycursor.execute(sql_query, (url, metatitle, metadata, metatitle, metadata))
        self.mydb.commit()

