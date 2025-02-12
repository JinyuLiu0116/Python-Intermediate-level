import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'doctor'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Query failed at {e}")

#Print all INS records for State = “NY” 
query = """SELECT * FROM ins WHERE state = 'NY';"""
print(f"#1: {query_mysql_executor(query=query,conn=conn)}")
