import csv
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'company'
)

data = [
    {"id":101, "name":'Jinyu Liu', "age":55},
    {"id":102, "name":'Qinyu Qiu', "age":45},
    {"id":103, "name":'Tinyu Tiu', "age":35},
    {"id":104, "name":'Binyu Biu', "age":25}
]

with open('data.csv', mode= 'w', newline='') as file:
    fieldnames = ["id", "name", "age"]
    writer= csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

def query_mysql_executor(query, conn):
    result = None
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    for row in result:
        print(row)

#Create a table: Ensure the table structure matches the CSV data format.
query1 = """CREATE TABLE people (
	        id INT PRIMARY KEY,
            name VARCHAR(225),
            age INT);"""
query_mysql_executor(query=query1, conn=conn)


if conn:
    conn.close()
