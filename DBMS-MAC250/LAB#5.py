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
        for row in result:
            print(row)
        print("--------------------------------------------------------------------")
    except Exception as e:
        print(f"query failed: {e}")

# Use the Premiere Products database to complete the following exercises.
# If directed to do so by your instructor, use the information provided with
# Exercises to print your output

# 1.List the part number and description for all parts. The part descriptions
# should appear in uppercase letters.
query1 = """SELECT partNum, UPPER(description) FROM part;"""
query_mysql_executor(query=query1, conn=conn)

# 2.List the customer number and name for all customers located in the
# city of Grove. Your query should ignore case. For example, a customer with th
# city Grove should be included as should customers whose city is GROVE, grove, GrOvE, and so on
query2 = """SELECT customerNum, customerName FROM customer WHERE city LIKE 'grove';"""
query_mysql_executor(query=query2, conn=conn)
