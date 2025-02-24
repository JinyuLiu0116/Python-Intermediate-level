import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'library'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        for row in result:
            print(row)
        print('-----------------------------------------------')
    except Exception as e:
        print(f"query failed: {e}")
        
if conn:
    conn.close()
