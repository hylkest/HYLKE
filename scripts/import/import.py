import mysql.connector
import os
from dotenv import load_dotenv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="Filename")
args = parser.parse_args()


with open(f'{args.file}', 'r') as txtfile:
    urllist = txtfile.read().splitlines()

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
for url in urllist:
    mycursor.execute(sql_query, (url,))

mydb.commit()

print(f"{len(urllist)} URLS added.")
