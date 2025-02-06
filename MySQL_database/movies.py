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

#Find all the WALL-* movies
query4 = """SELECT * FROM movies WHERE title LIKE '%WALL-%';"""
print(f"#4. {query_mysql_executor(query4, conn=conn)}")

#List all directors of Pixar movies (alphabetically), without duplicates
query5 = """SELECT DISTINCT director FROM movies ORDER BY director ASC;"""
print(f"#5. {query_mysql_executor(query5, conn=conn)}")

#List the last four Pixar movies released (ordered from most recent to least)
query6 = """SELECT title, year FROM movies ORDER BY year DESC LIMIT 4;"""
print(f"#6. {query_mysql_executor(query6, conn=conn)}")

#List the first five Pixar movies sorted alphabetically
query7 = """SELECT * FROM movies ORDER BY title ASC LIMIT 5;"""
print(f"#7. {query_mysql_executor(query7, conn=conn)}")

#List the next five Pixar movies sorted alphabetically
query8 = """SELECT title FROM movies ORDER BY title ASC LIMIT 5 OFFSET 5;"""
print(f"#8. {query_mysql_executor(query8, conn=conn)}")



if conn:
    conn.close()
