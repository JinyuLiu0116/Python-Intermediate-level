import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'doctor'
)

def query_mysql_executor(query, conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
    except Exception as e:
        raise Exception(f"query is failed at:{e}")
    

