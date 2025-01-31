import mysql.connector

def query_mysql_executor(query):
    conn = None
    cursor = None
    result = None
    conn = mysql.connector.connect(
        host ='localhost',
        user = 'root',
        password = '8551649',
        database = 'premiere'
    )
    if conn:
        print('Connection has been built')
    
    cursor = conn.cursor()
    if cursor:
        print('Cursor has been created')

    query = query
    cursor.execute(query)
    result = cursor.fetchall()
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    return result
