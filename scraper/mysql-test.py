import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("SQL_HOST"),
    user=os.getenv("SQL_USERNAME"),
    password=os.getenv("SQL_PASSWORD"),
    database=os.getenv("SQL_DB"),
    port=3306
)

mycursor = mydb.cursor()

sql_query = "INSERT INTO links (url) VALUES (%s)"
val = ("Test.nl",)
mycursor.execute(sql_query, val)

mydb.commit()

print("Data succesvol ingevoegd!")
