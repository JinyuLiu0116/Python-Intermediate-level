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

#Upload CSV data: Use the LOAD DATA INFILE statement to import the CSV data into the specific table.
query2 = """LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/data.csv'
            INTO TABLE company.people
            FIELDS TERMINATED BY ','
            ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;"""
query_mysql_executor(query=query2, conn=conn)

# Task 4: Backup and Restore Database 
# 1.	Backup the database: Use the mysqldump utility to create a backup of the database. 
command = 'cd C:\Program Files\MySQL\MySQL Workbench 8.0\ '
command = 'mysqldump -u root -p company > "C:\Users\ojin0\Downloads\company.sql"'


if conn:
    conn.close()
