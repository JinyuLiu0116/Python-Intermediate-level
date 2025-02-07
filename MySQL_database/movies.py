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

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'north_american_cities'
)

#List all the Canadian cities and their populations
query9 = """SELECT city, population FROM North_american_cities WHERE country = "Canada";"""
print(f"#9. {query_mysql_executor(query9, conn=conn)}")

#Order all the cities in the United States by their latitude from north to south
query10 = """SELECT city FROM North_american_cities WHERE country = "United States" ORDER BY latitude DESC;"""
print(f"#10. {query_mysql_executor(query10, conn=conn)}")

#List all the cities west of Chicago, ordered from west to east
query11 = """SELECT city FROM North_american_cities WHERE longtiude < (SELECT longtiude FROM North_american_cities WHERE city = 'Chicago' ORDER BY ASC);"""
print(f"#11. {query_mysql_executor(query11, conn=conn)}")

#List the two largest cities in Mexico (by population)
query12 = """SELECT city, population FROM North_american_cities WHERE country = 'Mexico' ORDER BY population DESC LIMIT 2;"""
print(f"#12. {query_mysql_executor(query12, conn=conn)}")


if conn:
    conn.close()
