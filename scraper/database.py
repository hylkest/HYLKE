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

    def insert_link(self, base_url, url):
        sql_query = "INSERT INTO links (base_url, url) VALUES (%s, %s)"
        try:
            self.mycursor.execute(sql_query, (base_url, url,))
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

    def insert_pagetitle(self, url, pagetitle):
        sql_query = "INSERT INTO pagetitle (pagetitle, url) VALUES (%s, %s)"
        try:
            self.mycursor.execute(sql_query, (pagetitle,url,))
            self.mydb.commit()
            print(f"Done scraping: {url}")
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

    def insert_metadata(self, url, metadata):
        sql_query = "INSERT INTO meta (url, meta_title, meta_description) VALUES (%s, %s, %s)"
        try:
            self.mycursor.execute(sql_query, (url, "test", metadata))
            self.mydb.commit()
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
