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

query1 = ("SELECT id, title FROM movie WHERE id = 6")
query_mysql_executor(query=query1, conn=conn)


query2 = ("SELECT year, title FROMR movie WHERE year BETWEEN 2000 AND 2010")
query_mysql_executor(query=query2, conn=conn)

    
query3 = ("SELECT year, title FROM movie WHERE year < 2000 or year > 2010")
query_mysql_executor(query=query3, conn=conn)


query4 = ("SELECT title, year FROM movie WHERE year <= 2003")
query_mysql_executor(query=query4, conn=conn)


if conn:
    conn.close()
