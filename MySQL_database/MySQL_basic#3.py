import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "8551649",
    database = "practice"
)

def query_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"query failed at: {e}")

query1 = "SELECT * FROM movie"
result = query_exexutor(query=query1, conn=conn)
for row in result:
    print(row)

cursor.execute("SELECT title FROM movie")
result_title=cursor.fetchall()
print("The title of movies:")
for row in result_title:
    print(row)

cursor.execute("SELECT director FROM movie")
result_director=cursor.fetchall()
print("The director of movies:")
for row in result_director:
    print(row)

cursor.execute("SELECT title,director FROM movie")
result_T_D=cursor.fetchall()
print("The title and director of movies:")
for row in result_T_D:
    print(row)

cursor.execute("SELECT titile,year FROM movie")
result_T_Y=cursor.fetchall()
print("The title and year of movies:")
for row in result_T_Y:
    print(row)

cursor.close()
conn.close()
