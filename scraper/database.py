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

    def insert_link(self, url):
        sql_query = "INSERT INTO links (url) VALUES (%s)"
        try:
            self.mycursor.execute(sql_query, (url,))
            self.mydb.commit()
            print(f"Link opgeslagen in database: {url}")
        except mysql.connector.Error as err:
            print(f"Databasefout: {err}")
