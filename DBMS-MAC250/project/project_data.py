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
        conn.commit()   
    except Exception as e:
        print(f"query is failed at:{e}")
    
query = """INSERT INTO ins VALUES
            ('GHI', 'Group Health Insurance', '11-11 11th st', 'Longisland City','NY','11101'),
            ('BC', 'Blue Cross', '22-22 22th st', 'Sunnyside','NY','11102'),
            ('AHS', 'American Health System', '33-33 33th st', 'Woodside','NY','11103');"""
query_mysql_executor(query=query,conn=conn)


if conn:
    conn.close()
