import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practice"
)

def query_excutor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"query failed at: {e}")

query1 = "SELECT * FROM movie"
result = query_excutor(query=query1, conn=conn)
for row in result:
    print(row)

query2 = "SELECT title FROM movie"
result = query_excutor(query=query2, conn=conn)
for row in result:
    print(row)

query3 = "SELECT director FROM movie"
result = query_excutor(query=query3, conn=conn)
for row in result:
    print(row)

query4 = "SELECT title,director FROM movie"
result = query_excutor(query=query4, conn=conn)
for row in result:
    print(row)

query5 = "SELECT titile,year FROM movie")
result = query_excutor(query=query5, conn=conn)
for row in result:
    print(row)

conn.close()
