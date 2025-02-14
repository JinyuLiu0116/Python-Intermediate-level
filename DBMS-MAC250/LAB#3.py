import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8551649',
    database = 'premiere'
)

def query_mysql_executor(query, conn):
    result = None
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Query failed at: {e}")
query1 = """CREATE TABLE nonappliance(
            partNum CHAR(4) PRIMARY KEY,
            description CHAR(15),
            onHand DECIMAL(4,0),
            class CHAR(2),
            price DECIMAL(6,2));"""
print(f"#1: {query_mysql_executor(query=query1, conn=conn)}")

# Insert into the nonappliance table the part number, part description, number of units on hand, item class,
# and unti price from the PART table for each part that is not in item class AP
query2 = """INSERT INTO nonappliance SELECT partNum, description, onHand, class, price FROM part WHERE class != 'AP';"""
print(f"#2: {query_mysql_executor(query=query2, conn=conn)}")
