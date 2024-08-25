import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practice"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS practice")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movie(
    Id INT PRIMARY KEY,
    Title VARCHAR(64),
    Director VARCHAR(64),
    Year INT,
    Length_minutes INT);
""")

cursor.execute("DESCRIBE movie")

for i in cursor:
    print(i,end=" ")

cursor.execute()

