import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("SQL_HOST"),
    user=os.getenv("SQL_USERNAME"),
    password=os.getenv("SQL_PASSWORD"),
    port=3306
)

print(mydb)