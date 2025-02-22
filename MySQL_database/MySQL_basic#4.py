import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practicebase"
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        for row in result:
            print(row)

cursor.execute("SELECT id, title FROM movie WHERE id = 6")
result1 = cursor.fetchall()


cursor.execute("SELECT year, title FROMR movie WHERE year BETWEEN 2000 AND 2010")
result2 = cusor.fetchall()

    
cursor.execute("SELECT year, title FROM movie WHERE year < 2000 or year > 2010")
result3 = cursor.fetchall()


cursor.execute("SELECT title, year FROM movie WHERE year <= 2003")
result4 = cursor.fetchall()


if conn:
    conn.close()
