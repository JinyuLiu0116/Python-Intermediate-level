import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='8551649',
            database='premiere'
        )
        print("Connection has been built")
        return conn
    except mysql.connector.Error as e:
        raise Exception(f"Database connection failed: {e}")

def execute_query(query):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        print('Cursor has been built')

        query = 'SELECT partNum, description, price FROM part;'
        cursor.execute(query)
        
        result = cursor.fetchall()
        return result

    except Exception as e:
        raise Exception(f"Job Failed {e}")

    finally:
        if cursor:
            cursor.close()
            print('Cursor has been closed')
        if conn:
            conn.close()
            print('Connection has been closed')
