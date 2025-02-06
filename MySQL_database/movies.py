import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'movies'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except Exception as e:
        raise Exception(f"query failed {e}")

#Find all the Toy Story movies      
query1 = """SELECT * FROM movies WHERE title LIKE '%Toy Story%';"""
print(f"#1. {query_mysql_executor(query1, conn=conn)}")

#Find all the movies directed by John Lasseter
query2 = """SELECT * FROM movies WHERE director = 'John Lasseter';"""
print(f"#2. {query_mysql_executor(query2, conn=conn)}")

#Find all the movies (and director) not directed by John Lasseter
query3 = """SELECT title, director FROM movies WHERE director != 'John Lasseter';"""
print(f"#3. {query_mysql_executor(query3, conn=conn)}")
