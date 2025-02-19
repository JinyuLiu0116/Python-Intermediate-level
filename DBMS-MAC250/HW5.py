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


if conn:
    conn.close()
