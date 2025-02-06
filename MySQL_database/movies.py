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
