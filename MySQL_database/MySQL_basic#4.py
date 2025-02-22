import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practicebase"
)

def query_mysql_executor(query, conn):
    
cursor = conn.cursor()

cursor.execute("SELECT id, title FROM movie WHERE id = 6")
result1 = cursor.fetchall()
for i in result1:
    print(i)

cursor.execute("SELECT year, title FROMR movie WHERE year BETWEEN 2000 AND 2010")
result2 = cusor.fetchall()
for i in result2:
    print(i)
    
cursor.execute("SELECT year, title FROM movie WHERE year < 2000 or year > 2010")
result3 = cursor.fetchall()
for i in result3:
    print(i)

cursor.execute("SELECT title, year FROM movie WHERE year <= 2003")
result4 = cursor.fetchall()
for i in result4:
    print(i)

cursor.close()
conn.close()
