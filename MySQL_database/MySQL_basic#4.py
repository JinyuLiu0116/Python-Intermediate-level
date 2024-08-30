import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practicebase"
)

cursor = conn.cursor()

cursor.execute("SELECT id, title FROM movie WHERE id = 6")
print(cursor)

cursor.execute("SELECT year, title FROMR movie WHERE year BETWEEN 2000 AND 2010")
print(cursor)

cursor.execute("SELECT year, title FROM movie WHERE year < 2000 or year > 2010")
print(cursor)

cursor.execute("SELECT title, year FROM movie WHERE year <= 2003")
print(cursor)

cursor.close()
conn.close()