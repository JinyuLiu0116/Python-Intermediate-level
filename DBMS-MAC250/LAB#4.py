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
    except Exception as e:
        print(f"query failed:{e}")

# 1 Create a view named major_customer. It consists of the customer number, name, balance, credit limit, 
# and rep number for every customer whose credit limit is $10000 or less.
# a.	Write and execute the CREATE VIEW command to create the major_customer view.
query1_a = """CREATE VIEW major_customer 
                AS SELECT customerNum, customerName, balance, creditLimit, repNum
                FROM customer
                WHERE creditLimit <= 10000;"""
query_mysql_executor(query= query1_a, conn=conn)

# b.Write and execute the command to retrieve the customer number and name of each customer 
# in the major_curstomer view with a balance that exceeds the credit limit.
query1_b = """SELECT customerNum, customerName FROM major_customer
                WHERE balance > creditLimit;"""
query_mysql_executor(query= query1_b, conn=conn)

#c.	Write and execute the query that the DBMS actually executes.
query1_c = """UPDATE major_customer 
                SET creditLimit = 10000
                WHERE customerNum = '148';"""
query_mysql_executor(query= query1_c, conn=conn)

if conn:
    conn.close()
