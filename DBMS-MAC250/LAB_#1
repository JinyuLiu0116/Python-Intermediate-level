import mysql.connector
conn = None
cursor = None
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '8551649',
        database = 'premiere'
    )
    if conn:
        print('Connection has been built')

    cursor = conn.cursor()
    if cursor:
        print('Cursor has been built')

#List the part number, description, and price for part.
    query = 'SELECT partNum, description, price FROM part'
    cursor.execute(query)
    
    result = cursor.fetchall()

    for row in result:
        print(row)

except Exception as e:
    raise Exception(f"Job Failed {e}")

finally:
    if cursor:
        cursor.close()
        print('Cursor has been closed')
    if conn:
        conn.close()
        print('Connection has been closed')
